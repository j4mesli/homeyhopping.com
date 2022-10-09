<?php
$output1 = null;
$retval = null;
$a = array($command1, $command2, $command3, $command4, $output);
$command1 = exec('python /spiders/webcrawlerApartmentFinder.py', $output);
$command2 = exec('python /spiders/webcrawlerApartments.py', $output);
$command3 = exec('python /spiders/webcrawlerNYRENTOWNSELL.py', $output);
$command4 = exec('python /update.py', $output);
var_dump($a);
?>