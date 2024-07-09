"use client";
import { useState, useEffect } from "react";
import api from "../api";
import "../styles/Home.css";
import Chart from "./Chart";
import React, { PureComponent } from "react";

function Home() {
  const [playlisturl, setPlaylistUrl] = useState("");
  const [videourl, setVideoUrl] = useState("");
  const [positive, setPositive] = useState();
  const [negative, setNegative] = useState();

  const sendplaylistUrl = (e) => {
    console.log(playlisturl);
    e.preventDefault();
    api
      .post("/api/processPlaylistURL/", { playlisturl })
      .then((res) => {
        setPositive(res.data.positive);
        setNegative(res.data.negative);
        if (res.status === 200) alert("Url Sent");
        else if (res.status === 400) alert("Bad Request");
        else alert("Failed to process url.");
      })
      .catch((error) => alert(error));
  };

  const sendVideoUrl = (e) => {
    console.log(videourl);
    e.preventDefault();
    api
      .post("/api/processVideoURL/", { videourl })
      .then((res) => {
        setPositive(res.data.positive);
        setNegative(res.data.negative);
        if (res.status === 200) alert("Url Sent");
        else if (res.status === 400) alert("Bad Request");
        else alert("Failed to process url.");
      })
      .catch((error) => alert(error));
  };

  return (
    <div>
      <h1>Youtube Comments Analyzer</h1>
      <br />
      <form onSubmit={sendVideoUrl}>
        <label htmlFor="title">Enter youtube video url:</label>
        <br />
        <input
          type="text"
          id="video_url"
          name="video_url"
          required
          onChange={(e) => setVideoUrl(e.target.value)}
          value={videourl}
        />
        <br />
        <input type="submit" value="Submit"></input>
      </form>
      <br />
      <form onSubmit={sendplaylistUrl}>
        <label htmlFor="title">Enter youtube playlist url:</label>
        <br />
        <input
          type="text"
          id="playlist_url"
          name="playlist_url"
          required
          onChange={(e) => setPlaylistUrl(e.target.value)}
          value={playlisturl}
        />
        <input type="submit" value="Submit"></input>
      </form>
      <div align="center">
        <Chart positive={positive} negative={negative} />
      </div>
    </div>
  );
}
export default Home;
