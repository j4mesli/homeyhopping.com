<?php
$output1 = null;
$retval = null;
$command1 = exec('usr/bin/python /spiders/webcrawlerApartmentFinder.py', $output);
$command2 = exec('usr/bin/python /spiders/webcrawlerApartments.py', $output);
$command3 = exec('usr/bin/python /spiders/webcrawlerNYRENTOWNSELL.py', $output);
$command4 = exec('usr/bin/python /update.py', $output);
$a = array($command1, $command2, $command3, $command4, $output);
try {
  var_dump($a);
  die("UPDATE COMPLETE");
}
catch (Exception e) {
  die("ERROR: " + e);
}
?>
