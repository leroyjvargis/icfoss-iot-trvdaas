<?php
$link = mysqli_connect('localhost', 'root', 'root', 'TRVDaA') or die("MySQL Error: " . mysql_error());
?>

<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>Traffic Rule Violation and Detection System</title>

<link href="css/skeleton.css" rel="stylesheet" type="text/css" media="all" />
</head>


<body>  
<div id="head">
 <div id="head_cen">
  <div id="head_sup" >
   
    

<div id="main">
 <div id="content" style = "width:800px:height:1200px;">
 <h1 style = "padding: 20px; font-size:40px; line-height:1em; text-align: center; color: #31a1ff;">Log</h1>
<table>
	<thead>
		<tr>
			<th><h1>SL</h1></th>
			<th><h1>Location Coordinates</h1></th>
			<th><h1>Location Name</h1></th>
			<th><h1>Timestamp</h1></th>
			<th><h1>Entry</h1></th>
		</tr>
	</thead>
	<tbody>

<?php
	$result = mysqli_query($link, "SELECT * FROM db ORDER BY timestamp ASC");
	while($pos = mysqli_fetch_assoc($result))
    {
    	
?>
		<tr>
			<td><?php echo $pos['sl']; ?></td>
			<td><?php echo $pos['loc_coord']; ?></td>
			<td><?php echo $pos['loc_name']; ?></td>
			<td><?php echo $pos['timestamp']; ?></td>
			<td><?php echo $pos['offense']; ?></td>
		</tr>
	</tbody>
<?php
	}
?>

</table>
</div
></body>
</html>