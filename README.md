# Wox.Plugin.WolframAlpha
=================================================
Note from @JakubKoralewski: 
- removed ability to copy cause `clipboard` is not compatible with newer Pythons
  - instead on click it takes you to wolfram search with that input 

[Wolfram Alpha](https://www.wolframalpha.com/) plugin for the [Wox launcher](https://github.com/Wox-launcher/Wox)  
Author: Edris Tavoosi

### About
Wox Plugin written in python to query Wolfram alpha.  
Answer in main window and full results in context menu.  

### Usage
Enter the keyword `wolfram` followed by your query.  
![open wolframalpha.com in default browser](https://raw.githubusercontent.com/EdrisT/Wox.Plugin.WolframAlpha/master/Screenshot1.png)  

The "Short answer" is displayed in the main window.  
![query search](https://raw.githubusercontent.com/EdrisT/Wox.Plugin.WolframAlpha/master/Screenshot2.png)
![query search](https://raw.githubusercontent.com/EdrisT/Wox.Plugin.WolframAlpha/master/Screenshot4.png) 

To see "Full results", open context menu.  
![Context menu](https://raw.githubusercontent.com/EdrisT/Wox.Plugin.WolframAlpha/master/Screenshot3.png)  

Select any answer to copy it to the clipboard.  

### Notice
Make sure the following python modules are installed: wolframalpha, clipboard, webbrowser, urllib.parse, requests  
They can be installed with pip command `pip install wolframalpha clipboard webbrowser urllib.parse requests`  

You have to get your own wolframalpha appid from `http://products.wolframalpha.com/api/` for this plugin to work.  
It's free and it only takes 1 minute to register.  
Put your appid in the `app_id` variable in main.py.  
The plugin detects if no appid is registered, and takes you to a webpage where you can get one.  