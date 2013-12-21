open (INFILE, "<respondent5.txt") || die "cannot open file";
my $sql_prefix="";
my $q_id = 0;
my $response_value = 0;
$sql_prefix = "insert into survey_data_quant (survey_id, update_user_id, update_timestamp, scale_id, q_id, form_seq_no, response_value ) values " .
	" ( 794, 'conv', getdate(), ";

while ( <INFILE> )
{
    ($pid, $one, $two, $four, $five, $six, $seven, $eight, $nine, $ten, $eleven, $twelve, $thirteen, $fourteen, $fifteen, $sixteen, $seventeen, $eighteen, $nineteen, $twenty) = split ('\t');
    #print "$pid $one $two $four $five $six \n";

    next if ( $pid =~ m/PID/);
   
    $q_id = 0;


    print " $sql_prefix 1, 6, $pid, $six ) ; \n ";
    print " $sql_prefix 1, 7, $pid, $seven ) ; \n ";
    print " $sql_prefix 1, 8, $pid, $eight ) ; \n ";
    print " $sql_prefix 1, 9, $pid, $nine ) ; \n ";
    print " $sql_prefix 1, 10, $pid, $ten ) ; \n ";
    print " $sql_prefix 1, 11, $pid, $eleven ) ; \n ";
    print " $sql_prefix 1, 12, $pid, $twelve ) ; \n ";
    print " $sql_prefix 1, 13, $pid, $thirteen ) ; \n ";
    print " $sql_prefix 1, 14, $pid, $fourteen ) ; \n ";
    print " $sql_prefix 1, 15, $pid, $fifteen ) ; \n ";




    print " $sql_prefix 2, 16, $pid, " . getval($sixteen ) . " ); \n ";
    print " $sql_prefix 2, 17, $pid, " . getval($seventeen ) . " ); \n ";
    print " $sql_prefix 2, 18, $pid, " . getval($eighteen ) . " ); \n ";
    print " $sql_prefix 2, 19, $pid, " . getval($nineteen ) . " ); \n ";
    print " $sql_prefix 2, 20, $pid, " . getval($twenty ) . " ); \n ";


} 

close (INFILE);


sub getval()
{
    $val = shift;
    if ($val == -100 ) { return 1; }
    if ($val == -50 ) { return 2; }
    if ($val == 0 ) { return 3; }
    if ($val == 50 ) { return 4; }
    if ($val == 100 ) {return 5; }
}
