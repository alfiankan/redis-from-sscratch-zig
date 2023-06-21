import redis
from typing import Dict 
from uuid import uuid4
import time
import traceback
from supabase import create_client, Client
import os
from postgrest.base_request_builder import APIResponse
import subprocess
#postgrest.base_request_builder.APIResponse

def send_score(scores: list, logs: str, time_elapsed_millis: int):
    print("Sending score to supabase")
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    github_repo: str = os.environ.get("GITHUB_REPO_URL")
    supabase: Client = create_client(url, key)

    participant: APIResponse = supabase\
        .table("score_board")\
        .select("*")\
        .eq("github_repository", github_repo)\
        .execute()

    if len(participant.data) == 0:
        raise Exception("Participant not found")

    participant = participant.data[0]
    print(len(logs))
    supabase\
        .table("attempts")\
        .insert({
            'score_board_id': participant["id"],
            'scores': scores,
            'test_output':  str(logs),
        }).execute()

    # count progress
    success = 0
    total = len(scores)
    for score in scores:
        if score["result"]:
            success += 1
    
    supabase.table("score_board").update({
        "scores": {"success": success, "total": total, "duration": time_elapsed_millis}
    }).eq("id", participant["id"]).execute()
    print("Done sending score to supabase")



def make_client() -> redis.Redis:
    return redis.Redis(host='redisnya', port=6379)

def test_case_ping_redis() -> bool:
    client = make_client()
    return client.ping()

def test_case_set_redis() -> bool:
    kv: Dict[str, str] = {
        str(uuid4()): "1",
        str(uuid4()): "2",
        str(uuid4()): "3",
        str(uuid4()): "4",
        str(uuid4()): "5",
    }

    client = make_client()
    for k, v in kv.items():
        if not client.set(k, v):
            return False

    for k, v in kv.items():
        if client.get(k).decode() != v:
            return False

    return True

def test_case_get_redis() -> bool:
    client = make_client() 

    key = str(uuid4())

    client.set(key, "1")

    if client.get(key).decode() != "1": 
        return False

    if client.get(f"{key}_#"):
        return False

    return True

def test_case_del_redis() -> bool:
    client = make_client()
    key = str(uuid4())

    client.set(key, "1")
    if client.get(key).decode() != "1":
        return False
    
    client.delete(key)

    if client.get(key):
        return False

    return True


def test_case_set_ttl() -> bool:
    client = make_client()
    key = str(uuid4())

    client.set(key, "2", ex=1)
    if not client.get(key):
        return False

    if client.get(key).decode() != "2":
        return False

    time.sleep(5)

    if client.get(key):
        return False

    return True


def main():
    
    results = []
    logs_errors = ""
    time_elapsed_millis = 0

    import datetime
    a = datetime.datetime.now()

    try:
        fn_res = test_case_ping_redis()
        results.append({"aspect": "[1] ping connection", "result": fn_res})
    except Exception as e:
        results.append({"aspect": "[1] ping connection", "result": False})
        logs_errors += str(e)
        logs_errors += traceback.format_exc()

    try:
        fn_res = test_case_set_redis()
        results.append({"aspect": "[2] set data", "result": fn_res})
    except Exception as e:
        results.append({"aspect": "[2] set data", "result": False})
        logs_errors += str(e)
        logs_errors += traceback.format_exc()

    try:
        fn_res = test_case_get_redis()
        results.append({"aspect": "[3] get data", "result": fn_res})
    except Exception as e:
        results.append({"aspect": "[3] get data", "result": False})
        logs_errors += str(e)
        logs_errors += traceback.format_exc()

    try:
        fn_res = test_case_del_redis()
        results.append({"aspect": "[4] delete data", "result": fn_res})
    except Exception as e:
        results.append({"aspect": "[4] delete data", "result": False})
        logs_errors += str(e)
        logs_errors += traceback.format_exc()

    try:
        fn_res = test_case_set_ttl()
        results.append({"aspect": "[5] TTL/Expiration", "result": fn_res})
    except Exception as e:
        results.append({"aspect": "[5] TTL/Expiration", "result": False})
        logs_errors += str(e)
        logs_errors += traceback.format_exc()

    b = datetime.datetime.now()
    delta = b - a
    time_elapsed_millis = int(delta.total_seconds() * 1000)

    # add executor logs

    logs_errors += subprocess\
                    .check_output(["docker", "logs", "redisnya"]).decode()

    print("Test Results:")
    print("=============")
    for i, res in enumerate(results):
        print(f"Test Case #{i+1}: {res}")

    print("Logs Errors:")
    print("============")
    print(logs_errors)

    send_score(results, logs_errors, time_elapsed_millis)


if __name__ == '__main__':
    main()
