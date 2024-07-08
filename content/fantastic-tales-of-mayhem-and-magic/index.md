+++
title = "Watch Fantastic Tales of Mayhem and Magic For Free | Kariboo XR Streaming"
date = "2024-07-08"
+++
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>

Experience Fantastic Tales of Mayhem and Magic Like Never Before with Kariboo!

<img src="https://filmhub-poster-server.b-cdn.net/aa3i-xzn3_fantastic_tales_of_mayhem_and_magic_16x9.jpg" alt="movie poster">

Step into a new dimension of movie watching with Kariboo, our innovative XR streaming app that brings your favorite films directly to your virtual reality headset. This week, we're highlighting Fantastic Tales of Mayhem and Magic, now available for streaming directly through Kariboo. Whether you're a long-time fan of the film or experiencing it for the first time, Kariboo allows you to transform any space into your own private cinema, offering a customizable viewing environment where you decide how and where you watch your movies.

<video id="video" width="100%" controls alt="movie trailer"></video>

At Kariboo, we’re committed to making high-quality entertainment accessible and free. You can stream Fantastic Tales of Mayhem and Magic at no cost, enjoying a cinema-like experience from the comfort of your own space. Whether you’re at home or on the go, as long as you have your VR headset, a captivating cinematic adventure is just a few clicks away.Getting started is easy:

1. Download the app: Available on major VR platforms, Kariboo is easy to set up. Just install the app from your VR device's app store.
2. Browse the library: Registration is free and you can immediately browse through an extensive collection of films, including classics, blockbusters, and hidden gems.
3. Select a movie: Find Fantastic Tales of Mayhem and Magic in the library and get ready to watch.
4. Enjoy Your Movie: Sit back, relax, and start streaming for free—you're in control of your viewing experience.

Join us at Kariboo and experience Fantastic Tales of Mayhem and Magic today. Happy viewing!

<script>
  var video = document.getElementById('video');
  if(Hls.isSupported()) {
    var hls = new Hls();
    hls.loadSource('https://vz-fb5092e4-932.b-cdn.net/e5ae5f88-3d71-49bc-ac20-960e486f55e9/playlist.m3u8');
    hls.attachMedia(video);
    hls.on(Hls.Events.MANIFEST_PARSED,function() {
      video.play();
  });
 }
 // hls.js is not supported on platforms that do not have Media Source Extensions (MSE) enabled.
 // When the browser has built-in HLS support (check using `canPlayType`), we can provide an HLS manifest (i.e. .m3u8 URL) directly to the video element throught the `src` property.
 // This is using the built-in support of the plain video element, without using hls.js.
  else if (video.canPlayType('application/vnd.apple.mpegurl')) {
    video.src = 'https://vz-fb5092e4-932.b-cdn.net/e5ae5f88-3d71-49bc-ac20-960e486f55e9/playlist.m3u8';
    video.addEventListener('canplay',function() {
      video.play();
    });
  }
</script>