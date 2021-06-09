const express = require("express"),
  app = express(),
  path = require("path");
(http = require("http").Server(app)),
  (socketio = require("socket.io")(http, {
    cors: {
      origin: "http://localhost:8080",
      methods: ["GET", "POST"],
      credentials: true,
    },
  }));

let position = {
  x: 100,
  y: 100,
};

app.use("/", express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

socketio.on("connection", (socket) => {
  console.log("a user connected");
  socket.emit("position", position);

  socket.on("move", (data) => {
    switch (data) {
      case "left":
        position.x -= 5;
        socketio.emit("position", position);
        break;
      case "right":
        position.x += 5;
        socketio.emit("position", position);
        break;
      case "top":
        position.y -= 5;
        socketio.emit("position", position);
        break;
      case "bottom":
        position.y += 5;
        socketio.emit("position", position);
        break;
    }
  });

  socket.on("disconnect", () => {
    console.log("user disconnected");
  });
});

http.listen(3000, () => {
  console.log("Listening at port 3000");
});
