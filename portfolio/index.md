---
layout: page
title: Portfolio
description: Portfolio of Kuprashevich Maksim
theme: red
---

Here you can find some examples of my projects.
There are three main sections here:

<details class="category">
<summary>Working projects</summary>
<p class="details">
Work projects, which were made during regular work. Big and long-term.
<br><br>
<a class="seventh before after" href="#odrs">Radar System</a> - Project that emulates object detection Radar System.
<br>
<a class="seventh before after" href="#dashcam">Navmii Dashcam</a> - Mobile ADAS system, 1.5 years project.
<br>
</p>
</details>

<div style="line-height:20%;">
    <br>
</div>

<details class="category">
<summary>Freelance projects</summary>
<p class="details">
Freelance projects, which were made during my free time as additional income. Usually little or middle size.
<br><br>
<a class="seventh before after" href="#gdocsearch">GDocSearch</a> - Live search through Google Drive documents.
<br>
<a class="seventh before after" href="#gametracker">GameTracker</a> - Game results tracker.
<br>
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
My own and training projects.
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
<div id="dashcam" style="">
<a name="dashcam"></a>
</div>

<h3 style="text-transform:uppercase;color:gray">Navmii Dashcam</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2015 - 2017</h5>
<span class="label btn-red">Machine Learning</span>
<span class="label btn-red">Image Processing</span>
<span class="label btn-red">OpenCV</span>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">Python</span>
<span class="label btn-red">Lua</span>
<span class="label btn-red">Torch</span>
<span class="label btn-red">Tensorflow</span>
<span class="label btn-red">Caffe</span>
<span class="label btn-red">Java</span>
<span class="label btn-red">Android</span>

Very big, long-term project on which I'm worked at Navmii company.
For a long time we developed ADAS [Advanced Drive Assistance System](https://en.wikipedia.org/wiki/Advanced_driver-assistance_systems) library for mobile platforms.

Main purpose was to create mobile application for Google Play and AppStore, but we also intagrated the library in a variety of other company projects.

So idea of main application is simple: user will be able to just download app to have system on his mobile phone that will warn him about collisions on road, signs, lanes and other dangers on road.

In Jule 2017 app was released for GooglePlay. [You can find it here](https://play.google.com/store/apps/details?id=com.navmii.android.dashcam&hl=ru).
You can find some screenshots of application here below. Also you can find there screenshots of world map with detected (purely on user mobile, without any other information!) signs. It fantastic, check it.

Many software utils were written during project, most interesting of them you can see also on screenshots below, so that project is not only about ADAS library, but also about many interesting ideas, tools, about research!

During project I worked with very much external tools and technologies: most of shallow ML methods, Deep Learning, Convolutional Networks, Caffe, Torch, OpenCV and Tensorflow frameworks, Image Processing methods, etc, etc. I even got a little experience of Android programming :)

On project working only 2 specialists, I and [Anton Varfolomeev](https://www.linkedin.com/in/dizvara/). Most of models were trained with data we collected and processed ourselves.

Here, on screenshots, you can find:
<ul>
<li>Video Detector - tool that plays videos and passes frames to networks. It can work with Caffe, Torch, Tensor models. Created for testing and debugging models, also for collecting new data. Here on screenshots presented mostly distance detection model.</li>
<li>Annotation Tool - tool for annotation frames with many classes. For SSD networks.</li>
<li>General Dashcam - mobile app with our library. Some of screenshot are with debug overlay to show you how it works. </li>
<li>Navmii labs - world map with signs that were collected from users.</li>
</ul>

On video there is another project with our library - Cocar.
It is very special version of our library because Cocar has 180 degree camera and very hard limitations of computational power.

<details class="screenshot" id="dashcam"><div class="gallery"><a target="_blank" href="/images/dashcam/2.jpg"><img src="/images/dashcam/2.jpg" width="300" height="200"></a><div class="desc">Distance detection process in VideoDetector</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/3.jpg"><img src="/images/dashcam/3.jpg" width="300" height="200"></a><div class="desc">Distance detection process in VideoDetector</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/04.jpg"><img src="/images/dashcam/04.jpg" width="300" height="200"></a><div class="desc">Distance detection process in VideoDetector</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/4.jpg"><img src="/images/dashcam/4.jpg" width="300" height="200"></a><div class="desc">Distance detection process in VideoDetector</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/5.jpg"><img src="/images/dashcam/5.jpg" width="300" height="200"></a><div class="desc">Distance detection process in VideoDetector</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/06.jpg"><img src="/images/dashcam/06.jpg" width="300" height="200"></a><div class="desc">VideoDetector program, main window</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/6.jpg"><img src="/images/dashcam/6.jpg" width="300" height="200"></a><div class="desc">VideoDetector program, some options</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/7.jpg"><img src="/images/dashcam/7.jpg" width="300" height="200"></a><div class="desc">VideoDetector program, some other options</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/11.jpg"><img src="/images/dashcam/11.jpg" width="300" height="200"></a><div class="desc">VideoDetector program, some other options</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/16.jpg"><img src="/images/dashcam/16.jpg" width="300" height="200"></a><div class="desc">Annotation tool, annotated frame</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/17.jpg"><img src="/images/dashcam/17.jpg" width="300" height="200"></a><div class="desc">Annotation tool, annotated frame</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/18.jpg"><img src="/images/dashcam/18.jpg" width="300" height="200"></a><div class="desc">Annotation tool, annotated frame</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/19.png"><img src="/images/dashcam/19.png" width="300" height="200"></a><div class="desc">NavmiiLabs, signs placed on map</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/20.png"><img src="/images/dashcam/20.png" width="300" height="200"></a><div class="desc">NavmiiLabs, signs placed on map</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/21.png"><img src="/images/dashcam/21.png" width="300" height="200"></a><div class="desc">NavmiiLabs, signs placed on map</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/22.png"><img src="/images/dashcam/22.png" width="300" height="200"></a><div class="desc">NavmiiLabs, signs placed on map</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/23.png"><img src="/images/dashcam/23.png" width="300" height="200"></a><div class="desc">NavmiiLabs, USA signs placed on map</div></div><div class="gallery"><a target="_blank" href="/images/dashcam/24.png"><img src="/images/dashcam/24.png" width="300" height="200"></a><div class="desc">Navmii AI Dashcam main page on GooglePlay</div></div>
<summary><div id="aligned-text">Screenshots</div></summary>
</details>
<div style="line-height:20%;">
    <br>
</div>
<details class="video">
<summary><div id="aligned-text">Videos</div></summary>
<iframe id="boarded-like-image" width="896" height="504" src="https://www.youtube.com/embed/1IFp6TRLK_o" frameborder="0" allowfullscreen></iframe>
</details>

<hr>





<!-- Just for navigation -->
<div id="odrs" style="">
<a name="odrs"></a>
</div>

<h3 style="text-transform:uppercase;color:gray">Radar System</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2015</h5>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">Network</span>
<span class="label btn-red">Low-Level Network</span>
<span class="label btn-red">HTML</span>
<span class="label btn-red">CSS</span>

Program that emulate radar system with very various options of radar parameters, painting options, reports and etc.
Was created to use in pair with modeling server, that calculate all math and physic, but I can't show that service because it is closed project
 and I have not it's sources. So, for presentation purposes I've created fake targets and recorded video. Enjoy it.

<i>Interface is only on Russian</i>

<details class="screenshot" id="odrs"><div class="gallery"><a target="_blank" href="/images/odrs/0.jpg"><img src="/images/odrs/0.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/odrs/2.jpg"><img src="/images/odrs/2.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/odrs/4.jpg"><img src="/images/odrs/4.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/odrs/5.jpg"><img src="/images/odrs/5.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/odrs/6.jpg"><img src="/images/odrs/6.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/odrs/7.jpg"><img src="/images/odrs/7.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/odrs/3242.jpg"><img src="/images/odrs/3242.jpg" width="300" height="200"></a><div class="desc">No description</div></div>
<summary><div id="aligned-text">Screenshots</div></summary>
</details>
<div style="line-height:20%;">
    <br>
</div>
<details class="video">
<summary><div id="aligned-text">Videos</div></summary>
<iframe id="boarded-like-image" width="896" height="504" src="https://www.youtube.com/embed/OS9GVCJooW0" frameborder="0" allowfullscreen></iframe>
</details>

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

<details class="screenshot" id="gdocsearch"><div class="gallery"><a target="_blank" href="/images/gdocsearch/ice_screenshot_20170226-194327.jpg"><img src="/images/gdocsearch/ice_screenshot_20170226-194327.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/gdocsearch/ice_screenshot_20170226-194353.jpg"><img src="/images/gdocsearch/ice_screenshot_20170226-194353.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/gdocsearch/ice_screenshot_20170226-194411.jpg"><img src="/images/gdocsearch/ice_screenshot_20170226-194411.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/gdocsearch/ice_screenshot_20170226-194431.jpg"><img src="/images/gdocsearch/ice_screenshot_20170226-194431.jpg" width="300" height="200"></a><div class="desc">No description</div></div>
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
<div id="gametracker" style="">
<a name="gametracker"></a>
</div>

<h3 style="text-transform:uppercase;color:gray">GameTracker</h3>
<h5 style="text-transform:uppercase;color:gray">Year 2017</h5>
<span class="label btn-red">C++</span>
<span class="label btn-red">Qt</span>
<span class="label btn-red">OpenCV</span>
<span class="label btn-red">Image Processing</span>
<span class="label btn-red">Network</span>
<span class="label btn-red">REST API</span>

Program that detect win or loose user in game. For now only Hearthstone is supported, but more game will be added in future.

Project was done for portal <a href="https://eloplay.com/" target="_blank" >Eloplay</a>. You can check there in downloads my tracker.

<details class="screenshot" id="gametracker"><div class="gallery"><a target="_blank" href="/images/gametracker/1.jpg"><img src="/images/gametracker/1.jpg" width="300" height="200"></a><div class="desc">No description</div></div>
<summary><div id="aligned-text">Screenshots</div></summary>
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

<details class="screenshot" id="youtube_downloader"><div class="gallery"><a target="_blank" href="/images/youtube_downloader/10.jpg"><img src="/images/youtube_downloader/10.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/youtube_downloader/11.jpg"><img src="/images/youtube_downloader/11.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/youtube_downloader/13.jpg"><img src="/images/youtube_downloader/13.jpg" width="300" height="200"></a><div class="desc">No description</div></div>
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

<details class="screenshot" id="wechat"><div class="gallery"><a target="_blank" href="/images/wechat/12.jpg"><img src="/images/wechat/12.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/wechat/13.jpg"><img src="/images/wechat/13.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/wechat/14.jpg"><img src="/images/wechat/14.jpg" width="300" height="200"></a><div class="desc">No description</div></div>
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

<details class="screenshot" id="video_uploader"><div class="gallery"><a target="_blank" href="/images/video_uploader/15.jpg"><img src="/images/video_uploader/15.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/video_uploader/16.jpg"><img src="/images/video_uploader/16.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/video_uploader/17.jpg"><img src="/images/video_uploader/17.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/video_uploader/18.jpg"><img src="/images/video_uploader/18.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/video_uploader/19.jpg"><img src="/images/video_uploader/19.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/video_uploader/20.jpg"><img src="/images/video_uploader/20.jpg" width="300" height="200"></a><div class="desc">No description</div></div>
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

<details class="screenshot" id="sattva"><div class="gallery"><a target="_blank" href="/images/sattva/21.jpg"><img src="/images/sattva/21.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/22.jpg"><img src="/images/sattva/22.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/23.jpg"><img src="/images/sattva/23.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/24.jpg"><img src="/images/sattva/24.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/25.jpg"><img src="/images/sattva/25.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/27.jpg"><img src="/images/sattva/27.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/28.jpg"><img src="/images/sattva/28.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/29.jpg"><img src="/images/sattva/29.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/30.jpg"><img src="/images/sattva/30.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/31.jpg"><img src="/images/sattva/31.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/32.jpg"><img src="/images/sattva/32.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/33.jpg"><img src="/images/sattva/33.jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/sattva/34.jpg"><img src="/images/sattva/34.jpg" width="300" height="200"></a><div class="desc">No description</div></div>
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

<details class="screenshot" id="proximity"><div class="gallery"><a target="_blank" href="/images/proximity/proxauth (1).jpg"><img src="/images/proximity/proxauth (1).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/proximity/proxauth (2).jpg"><img src="/images/proximity/proxauth (2).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/proximity/proxauth (3).jpg"><img src="/images/proximity/proxauth (3).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/proximity/proxauth (4).jpg"><img src="/images/proximity/proxauth (4).jpg" width="300" height="200"></a><div class="desc">No description</div></div>
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
<details class="screenshot" id="open_translate"><div class="gallery"><a target="_blank" href="/images/open_translate/open-tr (1).jpg"><img src="/images/open_translate/open-tr (1).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/open_translate/open-tr (2).jpg"><img src="/images/open_translate/open-tr (2).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/open_translate/open-tr (3).jpg"><img src="/images/open_translate/open-tr (3).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/open_translate/open-tr (4).jpg"><img src="/images/open_translate/open-tr (4).jpg" width="300" height="200"></a><div class="desc">No description</div></div>
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
<details class="screenshot" id="pandemic"><div class="gallery"><a target="_blank" href="/images/pandemic/pand (1).jpg"><img src="/images/pandemic/pand (1).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/pandemic/pand (2).jpg"><img src="/images/pandemic/pand (2).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/pandemic/pand (3).jpg"><img src="/images/pandemic/pand (3).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/pandemic/pand (4).jpg"><img src="/images/pandemic/pand (4).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/pandemic/pand (5).jpg"><img src="/images/pandemic/pand (5).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/pandemic/pand (6).jpg"><img src="/images/pandemic/pand (6).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/pandemic/pand (7).jpg"><img src="/images/pandemic/pand (7).jpg" width="300" height="200"></a><div class="desc">No description</div></div>
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

<details class="screenshot" id="ulmart"><div class="gallery"><a target="_blank" href="/images/ulmart/ulmart (1).jpg"><img src="/images/ulmart/ulmart (1).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/ulmart/ulmart (2).jpg"><img src="/images/ulmart/ulmart (2).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/ulmart/ulmart (3).jpg"><img src="/images/ulmart/ulmart (3).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/ulmart/ulmart (4).jpg"><img src="/images/ulmart/ulmart (4).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/ulmart/ulmart (5).jpg"><img src="/images/ulmart/ulmart (5).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/ulmart/ulmart (6).jpg"><img src="/images/ulmart/ulmart (6).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/ulmart/ulmart (7).jpg"><img src="/images/ulmart/ulmart (7).jpg" width="300" height="200"></a><div class="desc">No description</div></div><div class="gallery"><a target="_blank" href="/images/ulmart/ulmart (8).jpg"><img src="/images/ulmart/ulmart (8).jpg" width="300" height="200"></a><div class="desc">No description</div></div>
<summary><div id="aligned-text">Screenshots</div></summary>
</details>
