#_/_/_/_/_/_/_/_/_/_/#
#        �w�߂Q      #
#_/_/_/_/_/_/_/_/_/_/#

sub KING_COM2 {

	if($in{'mes'} eq ""){&ERR("�w�߂����͂���Ă��܂���B");}
	if(length($in{'mes'}) > 100) { &ERR("�莆�́A�S�p50�����ȉ��œ��͂��ĉ������B"); }
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xking ne $kid && $xgunshi ne $kid){&ERR("�����R�t�łȂ���Ύ��s�ł��܂���B");}

	if($xking eq $kid){
		$add = "�N��";
	}elsif($xgunshi eq $kid){
		$add = "�R�t";
	}

	$xmes = "$in{'mes'}($add:$kname���)";
	&COUNTRY_DATA_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>�w�߂���͂��܂����B</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�n�j"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;