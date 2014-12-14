VoiceServiceRTC
===============

Layout
----

![VoiceServiceRTC](https://farm6.staticflickr.com/5616/15044463343_14b6a585d6_o.png)

Features
----
  * Connect to a Android phone to get the voice recognition result
  * Send a string to Android phone then it will speak the text out

Requirements
----
  * Equipments
   * Android phone
    * Android 4.0.3 or later
    * [SL4A App](https://play.google.com/store/apps/details?id=org.androidideas.scriptlauncher)
  * OS
   * Linux Distributions
   * Windows
  * Softwares
   * OpenRTM-aist C++ 1.1 or later
   * CMake 2.8

Port
----

| Name     | Type          | Data Type   | Purpose |
| -------- | ------------- | ----------- | ------- |
| enable   | In       | RTC::TimedBoolean | Enable recognition |
| speech  | Out      | RTC::TimedString  | The recognition result |
| tts     | In      | RTC::TimedString   | The text to speech out        |

Usage
----

  1. Download and install SL4A on your Android phone
  2. Copy speech_gui.py and layout.xml in to your SD card

License
----

Licensed under the [Apache License, Version 2.0][Apache]  
Distributed under the [MIT License][mit].  
Dual licensed under the [MIT license][MIT] and [Apache License, Version 2.0][Apache].  
 
[Apache]: http://www.apache.org/licenses/LICENSE-2.0
[MIT]: http://www.opensource.org/licenses/mit-license.php
