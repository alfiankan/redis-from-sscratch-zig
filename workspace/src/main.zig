const std = @import("std");

const RedisServer = struct {
    stream_server: std.net.StreamServer,

    pub fn init() !RedisServer {
        var server = std.net.StreamServer.init(.{ .reuse_address = true });

        const address = std.net.Address.initIp4([4]u8{ 0, 0, 0, 0 }, 6379);

        try server.listen(address) catch |err| {
            std.log.fatal("Error : {s}\n", .{err});
        };
        return RedisServer{ .stream_server = server };
    }

    pub fn accept(self: *RedisServer) !void {
        const conn = try self.stream_server.accept();

        while (true) {
            var buf: [1024]u8 = undefined;
            const msg_size = try conn.stream.read(buf[0..]);

            std.log.info("Received: {s}\n", .{buf[0..msg_size]});

            const response = "+PONG\r\n";

            try conn.stream.write(response[0..]) catch |err| {
                std.log.fatal("Error : {s}\n", .{err});
            };
        }
    }
};

pub fn main() !void {
    var server = try RedisServer.init();
    defer server.stream_server.deinit();

    try server.accept() catch |err| {
        std.log.fatal("Error : {s}\n", .{err});
    };
}
