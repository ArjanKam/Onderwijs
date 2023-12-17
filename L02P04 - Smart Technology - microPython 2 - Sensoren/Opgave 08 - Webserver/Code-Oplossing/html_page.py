HTML = """<!DOCTYPE html>
<html>
   <head>
      <title>Pico Relay Control Web Server</title>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      
      <style>html{font-family: Arial; display:inline-block; margin: 0px auto; text-align: center;}
         h1{font-family: Arial; color: #2551cc;}
         .button1{-webkit-border-radius: 28; -moz-border-radius: 28; border-radius: 28px; font-family: Arial; color: #ffffff;
         font-size: 30px; background: #2ba615; padding: 10px 20px 10px 20px; text-decoration: none;}
         .button2{-webkit-border-radius: 28; -moz-border-radius: 28; border-radius: 28px; font-family: Arial; color: #ffffff;
         font-size: 30px; background: #f52e45; padding: 10px 20px 10px 20px; text-decoration: none;}
      </style>
   </head>
   <body>
      <h1>Pico Relay Control Web Server</h1>
      <p>%s</p>
      <p><a href="/relay/on1"><button class="button1">ON 1</button></a>
      <a href="/relay/off1"><button class="button2">OFF 1</button></a></p>
      <p><a href="/relay/on2"><button class="button1">ON 2</button></a>
      <a href="/relay/off2"><button class="button2">OFF 2</button></a></p>
      <p><a href="/relay/on3"><button class="button1">ON 3</button></a>
      <a href="/relay/off3"><button class="button2">OFF 3</button></a></p>
      <p><a href="/relay/on4"><button class="button1">ON 4</button></a>
      <a href="/relay/off4"><button class="button2">OFF 4</button></a></p>
      <p><a href="/relay/on5"><button class="button1">ON 5</button></a>
      <a href="/relay/off5"><button class="button2">OFF 5</button></a></p>
      <p><a href="/relay/on6"><button class="button1">ON 6</button></a>
      <a href="/relay/off6"><button class="button2">OFF 6</button></a></p>
      <p><a href="/relay/on7"><button class="button1">ON 7</button></a>
      <a href="/relay/off7"><button class="button2">OFF 7</button></a></p>
      <p><a href="/relay/on8"><button class="button1">ON 8</button></a>
      <a href="/relay/off8"><button class="button2">OFF 8</button></a></p>
   </body>
</html>
"""

