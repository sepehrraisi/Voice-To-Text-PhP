<?php
$output=null;
$retval=null;
exec("sudo python3 /var/www/html/Sadoos/ps.py", $output, $retval);
// echo "Returned with status $retval and output:\n";
// print_r(exec("cat /var/www/html/Sadoos/Res.txt"));
// print_r(exec("cat /var/www/html/Sadoos/Sites.txt"));
$R = (exec("cat /var/www/html/Sadoos/Res.txt"));
$S = (exec("cat /var/www/html/Sadoos/Sites.txt"));
$M = file_get_contents( "/var/www/html/Sadoos/Sites.txt" );
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
        <?php  echo $M; ?>
        <a href="https://demo.sadoos.ir/Sadoos/f.php" class="button-64">متخصصین آماده</a>
    </body>
</html>