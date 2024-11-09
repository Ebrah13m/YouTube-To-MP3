<h1> YouTube-To-MP3</h1>
A simple desktop application built with Python that allows you to download YouTube videos as MP3 files. The application features a clean, modern dark-themed GUI built with customtkinter.

<h1>Features</h1>
<ul>
  <li>Simple and intuitive user interface</li>
  <li>Dark mode support</li>
  <li>Direct YouTube URL input</li>
  <li>Automatic conversion to MP3 forma</li>
  <li>Clean file handling (temporary files are automatically removed)</li>
  <li>Error handling for invalid or unavailable videos</li>
</ul>

<h1>Prerequisites</h1>
Before running this application, make sure you have Python installed and the following dependencies:

pip install customtkinter
pip install pytube
pip install moviepy

<h1>Known Issues and Fixes</h1>
The application includes patches for common pytube issues related to YouTube's client version and throttling system. These fixes are implemented directly in the code to ensure stable functionality. However, please note:

  <ul>
    <li>YouTube regularly updates their systems, which may require updating these patches</li>
    <li>If downloads stop working, first check for updates to the client version numbers</li>
    <li>Current client version settings (as of last update):</li>
  </ul>

```python
*default*clients["ANDROID"]["context"]["client"]["clientVersion"] = "19.08.35"
*default*clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
*default*clients["ANDROID_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
*default*clients["IOS_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
*default*clients["IOS_MUSIC"]["context"]["client"]["clientVersion"] = "6.41"
```



  
