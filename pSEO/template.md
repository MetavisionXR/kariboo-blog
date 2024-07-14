+++
title = "Watch {{template_data.movie_title}} For Free | Kariboo XR Streaming"
date = "2024-07-08"
+++
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>

Experience {{template_data.movie_title}} Like Never Before with Kariboo!

<img src="{{template_data.poster_url}}" alt="movie poster" loading="lazy">

Step into a new dimension of movie watching with Kariboo, our innovative XR streaming app that brings your favorite films directly to your virtual reality headset. This week, we're highlighting {{template_data.movie_title}}, now available for streaming directly through Kariboo. Whether you're a long-time fan of the film or experiencing it for the first time, Kariboo allows you to transform any space into your own private cinema, offering a customizable viewing environment where you decide how and where you watch your movies.

{% if template_data.trailer_url is not none %}
<video id="video" width="100%" controls></video>
{% else %}
<div class="videoWrapper">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/S8wQ6Szlwkw?si=Jkibe-raLWK9uMYP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
{% endif %}

At Kariboo, we’re committed to making high-quality entertainment accessible and free. You can stream {{template_data.movie_title}} at no cost, enjoying a cinema-like experience from the comfort of your own space. Whether you’re at home or on the go, as long as you have your VR headset, a captivating cinematic adventure is just a few clicks away.

Getting started is easy:

1. Download the app: Available on major VR platforms, Kariboo is easy to set up. Just install the app from your VR device's app store.
2. Browse the library: Registration is free and you can immediately browse through an extensive collection of films, including classics, blockbusters, and hidden gems.
3. Select a movie: Find {{template_data.movie_title}} in the library and get ready to watch.
4. Enjoy Your Movie: Sit back, relax, and start streaming for free—you're in control of your viewing experience.

Join us at Kariboo and experience {{template_data.movie_title}} today. Happy viewing!

{% if template_data.trailer_url is not none %}  
<script>
  var video = document.getElementById('video');
  if(Hls.isSupported()) {
    var hls = new Hls();
    hls.loadSource('{{template_data.trailer_url}}');
    hls.attachMedia(video);
    hls.on(Hls.Events.MANIFEST_PARSED,function() {
      video.play();
  });
 }
 // hls.js is not supported on platforms that do not have Media Source Extensions (MSE) enabled.
 // When the browser has built-in HLS support (check using `canPlayType`), we can provide an HLS manifest (i.e. .m3u8 URL) directly to the video element throught the `src` property.
 // This is using the built-in support of the plain video element, without using hls.js.
  else if (video.canPlayType('application/vnd.apple.mpegurl')) {
    video.src = '{{template_data.trailer_url}}';
    video.addEventListener('canplay',function() {
      video.play();
    });
  }
</script>
{% else %}
<style>
.videoWrapper {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
}
.videoWrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
{% endif %}