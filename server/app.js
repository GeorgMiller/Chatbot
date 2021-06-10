const express = require("express"),
  app = express(),
  path = require("path"),
  fs = require("fs"),
  ms = require("mediaserver"),
  http = require("http").Server(app),
  socketio = require("socket.io")(http, {
    cors: {
      origin: "http://localhost:8080",
      methods: ["GET", "POST"],
      credentials: true,
    },
  });

const ss = require("socket.io-stream");

let position = {
  x: 100,
  y: 100,
};

// app.use("/", express.static("public"));

app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "/login.html"));
});

app.get("/game", (req, res) => {
  res.sendFile(path.join(__dirname, "/public/index_old.html"));
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

  socket.on("message", async function (data) {
    console.log(data);

    const dataURL = data.audio.dataURL.split(",").pop();
    let fileBuffer = Buffer.from(dataURL, "base64");
    console.log(fileBuffer);

    fs.writeFileSync("test.wav", fileBuffer, function (err) {
      res.sendStatus(err ? 500 : 200);
    });

    // ms.pipe("", "", path.join(__dirname, "/login.html"));

    const results = "HHHH";
    socket.emit("results", results);
  });
});

http.listen(3000, () => {
  console.log("Listening at port 3000");
});
