<?php
$P = (exec("cat /var/www/html/Sadoos/Amghezi.txt"));
?>


<!DOCYTPE html>
<html>
    <head>
        <title>Results</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" href="main.css">
    </head>
    <body style="background-image: url(bg.png);"><div class="center">
        <p style="color: white;"><?php  echo $P; ?></p>
    </body>
</html>