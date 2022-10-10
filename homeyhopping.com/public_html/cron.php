<?php
$output1 = null;
$retval = null;
$command1 = exec('usr/bin/python /spiders/webcrawlerApartmentFinder.py', $output);
$command2 = exec('usr/bin/python /spiders/webcrawlerApartments.py', $output);
$command3 = exec('usr/bin/python /spiders/webcrawlerNYRENTOWNSELL.py', $output);
$command4 = exec('usr/bin/python /update.py', $output);
$a = array($command1, $command2, $command3, $command4, $output);
var_dump($a);
?>
