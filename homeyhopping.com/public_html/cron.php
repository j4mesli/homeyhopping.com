<?php
$output1 = null;
$retval = null;
$command1 = exec('python /spiders/webcrawlerApartmentFinder.py', $output);
$command2 = exec('python /spiders/webcrawlerApartments.py', $output);
$command3 = exec('python /spiders/webcrawlerNYRENTOWNSELL.py', $output);
$command4 = exec('python /update.py', $output);
$a = array($command1, $command2, $command3, $command4, $output);
var_dump($a);
?>
