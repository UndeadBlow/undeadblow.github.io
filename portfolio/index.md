---
layout: page
title: Portfolio
description: Portfolio of Kuprashevich Maksim
theme: red
---

Here you can find some examples of my projects.
There are three main sections here:

<script>
<!-- function ready() {
  var subdirs = getSubdirs();

  for (var i = 0; i < subdirs.length; ++i) {
    var images = getImagesList(subdirs[i]);
    var spoiler_elems = document.getElementsByTagName('details');
    var spoiler_elem = null;
    for (var k = 0; k < spoiler_elems.length; ++k) {
      if (spoiler_elems[k].id == subdirs[i].substr(1)) {
        spoiler_elem = spoiler_elems[k];
      }
    }
    if (spoiler_elem == null) {
      return;
    }
    for (var j = 0; j < images.length; ++j) {
      spoiler_elem.innerHTML += "<img src=\"" + "/images" + subdirs[i] + images[j] + "\" class=\"img-boarded\">";
    }
  }
}

function getImagesList(subdir) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", '/images/' + subdir, false ); // false for synchronous request
  xmlHttp.send( null );
  var htmlObject = document.createElement('div')
  htmlObject.innerHTML = xmlHttp.responseText;

  var allElems = htmlObject.getElementsByClassName("name");
  var images = []
  for (var i = 0; i < allElems.length; ++i) {
    var elem = allElems[i];
    var href = elem.getElementsByTagName('a')[0].href
    if (href.indexOf('.png') < 0 && href.indexOf('.jpg') < 0
    && href.indexOf('.jpeg') < 0) {
      continue;
    } else {
      href = href.substr(href.lastIndexOf('/'));
      images.push(href);
    }
  }

  return images;
}

function getSubdirs() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", '/images', false ); // false for synchronous request
  xmlHttp.send( null );
  var htmlObject = document.createElement('div')
  htmlObject.innerHTML = xmlHttp.responseText;

  var allElems = htmlObject.getElementsByClassName("name");
  var dirs = []
  for (var i = 0; i < allElems.length; ++i) {
    var elem = allElems[i];
    var href = elem.getElementsByTagName('a')[0].href;
    if (href[href.length - 1] == "/") {
      href = href.substr(0, href.length - 1);
      dirs.push(href);
    }
  }

  var subdirs = []
  for (var i = 0; i < dirs.length; ++i) {
    if (dirs[i].split("/").length > 4) {
      subdirs.push(dirs[i].substr(dirs[i].lastIndexOf('/') ));
    }
  }
  return subdirs;
}

  document.addEventListener("DOMContentLoaded", ready); -->
</script>

<details class="category">
<summary>Working projects</summary>
<p class="details">
Work projects, which were made during regular work. Most of them is big and long-term.
<br><br>
</p>
</details>

<div style="line-height:20%;">
    <br>
</div>

<details class="category">
<summary>Freelance projects</summary>
<p class="details">
Freelance projects, which were made during my free time as additional income.
<br><br>
<a class="seventh before after" href="#wechat">WeChat</a> - Project for recording dialogs from Wechat service.
<br>
<a class="seventh before after" href="#youtube_downloader">YoutubeDownloader</a> - Downloading Youtube videos.
<br>
<a class="seventh before after" href="#video_uploader">VideoUploader</a> - Program that created for uploading videos to Yotuube, DailyMotion, Vimeo and Dropbox.
<br>
<a class="seventh before after" href="#sattva">SattvaMailer</a> - Messanger for social network VKontakte.
<br>
<a class="seventh before after" href="#proximity">ProximityAuth</a> - Servie for Biocad company that allow to use Biocad-cards for authorize in various programs and even login to Windows.
<br>
</p>
</details>

<div style="line-height:20%;">
    <br>
</div>

<details class="category">
<summary>Own and training projects</summary>
<p class="details">
My own projects and training projects. Usually such projects is unfinished and very rough.
<br><br>
<a class="seventh before after" href="#open_translate">OpenTranslate</a> - Chrome extension for translate ENG to RUS and save words to dictionary.
<br>
<a class="seventh before after" href="#pandemic">PandemicCalc</a> - Program with math model of diseases spreading.
<br>
<a class="seventh before after" href="#ulmart">UlmartMonitoring</a> - Bot for tracking goods availability and prices in Internet shop.
<br>
</p>
</details>
<br>
...or just navigate here all projects:

<hr>

<!-- Just for navigation -->
<div id="gdocsearch" style="">
<a name="gdocsearch"></a>
</div>
<!-- GDocSearch -->
<h3 style="text-transform:uppercase;color:gray">GDocSearch</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2017</h5>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">Network</span>
<span class="label btn-red">REST API</span>
<span class="label btn-red">HTML</span>

Program to live search in Google Documents, to copy rich text of sections that were found, to view it in web and etc.

<details class="screenshot" id="gdocsearch"> <img src="/images/gdocsearch/ice_screenshot_20170226-194327.png" class="img-boarded"> <img src="/images/gdocsearch/ice_screenshot_20170226-194353.png" class="img-boarded"> <img src="/images/gdocsearch/ice_screenshot_20170226-194411.png" class="img-boarded"> <img src="/images/gdocsearch/ice_screenshot_20170226-194431.png" class="img-boarded">
<summary><div id="aligned-text">Screenshots</div></summary>
</details>
<div style="line-height:20%;">
    <br>
</div>
<details class="video">
<summary><div id="aligned-text">Videos</div></summary>
<iframe id="boarded-like-image" width="896" height="504" src="https://www.youtube.com/embed/RBJry3_UYyU" frameborder="0" allowfullscreen></iframe>
</details>

<hr>

<!-- Just for navigation -->
<div id="youtube_downloader" style="">
<a name="youtube_downloader"></a>
</div>
<!-- Youtube Downloader -->
<h3 style="text-transform:uppercase;color:gray">Youtube Downloader</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2016</h5>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">Network</span>
<span class="label btn-red">HTML</span>

Simple freelance program for downloading videos from Youtube.
Working through parsing source code of Youtube, no API methods was used.

<details class="screenshot" id="youtube_downloader"> <img src="/images/youtube_downloader/10.png" class="img-boarded"> <img src="/images/youtube_downloader/11.png" class="img-boarded"> <img src="/images/youtube_downloader/13.png" class="img-boarded">
<summary><div id="aligned-text">Screenshots</div></summary>
</details>

<hr>

<!-- Just for navigation -->
<div id="wechat" style="">
<a name="wechat"></a>
</div>
<!-- WeChat -->
<h3 style="text-transform:uppercase;color:gray">WeChat</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2016</h5>
<a name="wechat"></a>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">HTML</span>
<span class="label btn-red">Network</span>
<span class="label btn-red">Javascript</span>

That freelance project was created to saving all the dialogs from WeChat to database.
So workflow is very simple, you run it, you login and you push Record button.
After that everything will happen in WeChat will be recorded.

<details class="screenshot" id="wechat"> <img src="/images/wechat/12.png" class="img-boarded"> <img src="/images/wechat/13.png" class="img-boarded"> <img src="/images/wechat/14.png" class="img-boarded">
<summary><div id="aligned-text">Screenshots</div></summary>
</details>

<hr>

<!-- Just for navigation -->
<div id="video_uploader" style="">
<a name="video_uploader"></a>
</div>
<!-- Video Uploader -->
<h3 style="text-transform:uppercase;color:gray">Video Uploader</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2016</h5>
<a name="video_uploader"></a>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">REST API</span>
<span class="label btn-red">Network</span>
<span class="label btn-red">Javascript</span>

That program was created to upload videos to Youtube, DailyMotion, Vimeo and Dropbox.
Workflow was desined as follows: you can choose video that you want to upload,
then you can choose service from described above and then you can configure some options.
After video is uploaded, you can't choose the same service again (blurred icon on the screenshots).

Working fully with API of listed services, no parsing code, only official methods.

It's really user-friendly and nice utility, with autofilling forms with information from video, animations, progress bar and etc.

<details class="screenshot" id="video_uploader"> <img src="/images/video_uploader/15.png" class="img-boarded"> <img src="/images/video_uploader/16.png" class="img-boarded"> <img src="/images/video_uploader/17.png" class="img-boarded"> <img src="/images/video_uploader/18.png" class="img-boarded"> <img src="/images/video_uploader/19.png" class="img-boarded"> <img src="/images/video_uploader/20.png" class="img-boarded">
<summary><div id="aligned-text">Screenshots</div></summary>
</details>

<hr>
<div id="sattva" style="">
<a name="sattva"></a>
</div>
<!-- SattvaMailer -->
<h3 style="text-transform:uppercase;color:gray">Sattva Mailer</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2013</h5>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">VK API</span>
<span class="label btn-red">HTML</span>
<span class="label btn-red">Javascript</span>
<span class="label btn-red">Network</span>
<span class="label btn-red">Webkit</span>

Messenger for <a href="https:\\vk.com">Vkontakte</a> (Russian social facebook-like network). Have huge functionality,
works with Vkontakte API and WebKit browser from Qt. Many challenges were solved through interaction with the Javascript code. Allows to work with
proxy and have flexible options. Supports many functions from site: add to friends, add friend to list, save all friends in file and many other automating options.

<i>Created for educational purposes, as example how to work with REST API</i>

<details class="screenshot" id="sattva"> <img src="/images/sattva/21.png" class="img-boarded"> <img src="/images/sattva/22.png" class="img-boarded"> <img src="/images/sattva/23.png" class="img-boarded"> <img src="/images/sattva/24.png" class="img-boarded"> <img src="/images/sattva/25.png" class="img-boarded"> <img src="/images/sattva/27.png" class="img-boarded"> <img src="/images/sattva/28.png" class="img-boarded"> <img src="/images/sattva/29.png" class="img-boarded"> <img src="/images/sattva/30.png" class="img-boarded"> <img src="/images/sattva/31.png" class="img-boarded"> <img src="/images/sattva/32.png" class="img-boarded"> <img src="/images/sattva/33.png" class="img-boarded"> <img src="/images/sattva/34.png" class="img-boarded">
<summary><div id="aligned-text">Screenshots</div></summary>
</details>


<hr>
<div id="proximity" style="">
<a name="proximity"></a>
</div>
<!-- ProximityAuth -->
<h3 style="text-transform:uppercase;color:gray">Proximity Auth</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2013</h5>
<span class="label btn-red">C</span>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">Win-API</span>
<span class="label btn-red">Network</span>
<span class="label btn-red">SQL</span>
<span class="label btn-red">DLL</span>

Project for Biocad company. For security purposes it is without much of details.

This software package allows Biocad-card users to safe run and authorize in various programs, list of which can be extended by admin with
plugins (using Dynamic Link Libraries). Also it allows to login in Windows with user card.
Project performed on Qt, but uses very low-level Windows tools, so it is not cross-platform.
Many changes was solved durig work, because app must be very safe and flexible, and main challenge was to secure card-software interaction, to prevent grabbing information with Low-Level Hooks in Windows.

<details class="screenshot" id="proximity"> <img src="/images/proximity/proxauth (1).png" class="img-boarded"> <img src="/images/proximity/proxauth (2).png" class="img-boarded"> <img src="/images/proximity/proxauth (3).png" class="img-boarded"> <img src="/images/proximity/proxauth (4).png" class="img-boarded">
<summary><div id="aligned-text">Screenshots</div></summary>
</details>

<hr>
<div id="open_translate" style="">
<a name="open_translate"></a>
</div>
<!-- Open Translate -->
<h3 style="text-transform:uppercase;color:gray">Open Translate</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2013</h5>
<span class="label btn-red">Javascript</span>
<span class="label btn-red">HTML</span>
<span class="label btn-red">CSS</span>

My own project that I sometimes developing in my spare time. This is the Google Chrome extension for translation english words and sentences on russian.
I started that project because current translators like LinguaLeo wants money for adding many words in your dictionary per day and I don't like it.

I have never worked before with Javascript, HTML and CSS before that project, but learned a few things in the process.
For translation this extension uses three servises (at now) with open API: <a href="https://translate.yandex.ru/">Yandex.Translate</a>, <a href="https://mymemory.translated.net/">MyMemory</a> and <a href="http://www.frengly.com/">Frengly</a>.
In the future, I'm planning to modify this exstension to save words to <a href="http://ankisrs.net/">Anki</a> format files to use it with this awesome program.
<details class="screenshot" id="open_translate"> <img src="/images/open_translate/open-tr (1).png" class="img-boarded"> <img src="/images/open_translate/open-tr (2).png" class="img-boarded"> <img src="/images/open_translate/open-tr (3).png" class="img-boarded"> <img src="/images/open_translate/open-tr (4).png" class="img-boarded">
<summary><div id="aligned-text">Screenshots</div></summary>
</details>


<hr>
<div id="pandemic" style="">
<a name="pandemic"></a>
</div>
<!-- Pandemic Calc -->
<h3 style="text-transform:uppercase;color:gray">Pandemic Calc</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2012</h5>
<a name="pandemic"></a>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">Math</span>

My training project within the discipline "Mathematic modeling".
This program allows to create and edit cities in which can be modeled (through the solution of differential equations) an epidemic of different diseases with different parameters.
Also it allows to output different plots.
<details class="screenshot" id="pandemic"> <img src="/images/pandemic/pand (1).png" class="img-boarded"> <img src="/images/pandemic/pand (2).png" class="img-boarded"> <img src="/images/pandemic/pand (3).png" class="img-boarded"> <img src="/images/pandemic/pand (4).png" class="img-boarded"> <img src="/images/pandemic/pand (5).png" class="img-boarded"> <img src="/images/pandemic/pand (6).png" class="img-boarded"> <img src="/images/pandemic/pand (7).png" class="img-boarded">
<summary><div id="aligned-text">Screenshots</div></summary>
</details>


<hr>
<div id="ulmart" style="">
<a name="ulmart"></a>
</div>
<!-- Ulmart Monitoring -->
<h3 style="text-transform:uppercase;color:gray">Ulmart Monitoring</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2011</h5>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">HTML</span>
<span class="label btn-red">Network</span>

My own project, that I wrote for myself. That program designed for parsing russian online shop "Ulmart" and monitoring prices for goods.
When amount of good or price changes - program notifies user about event in various ways (sound, colored row in table and tray message).
Program have different options, such as color setting, delay setting, sound enable\disable, etc.

<details class="screenshot" id="ulmart"> <img src="/images/ulmart/ulmart (1).png" class="img-boarded"> <img src="/images/ulmart/ulmart (2).png" class="img-boarded"> <img src="/images/ulmart/ulmart (3).png" class="img-boarded"> <img src="/images/ulmart/ulmart (4).png" class="img-boarded"> <img src="/images/ulmart/ulmart (5).png" class="img-boarded"> <img src="/images/ulmart/ulmart (6).png" class="img-boarded"> <img src="/images/ulmart/ulmart (7).png" class="img-boarded"> <img src="/images/ulmart/ulmart (8).png" class="img-boarded">
<summary><div id="aligned-text">Screenshots</div></summary>
</details>
