#_/_/_/_/_/_/_/_/_/_/#
#        �w�߂Q      #
#_/_/_/_/_/_/_/_/_/_/#

sub KING_COM5 {

	if($in{'mes'} eq ""){&ERR("�w�߂����͂���Ă��܂���B");}
	if(length($in{'mes'}) > 100) { &ERR("�莆�́A�S�p50�����ȉ��œ��͂��ĉ������B"); }
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	open(IN,"$COUNTRY_MES");
	@C_MES = <IN>;
	close(IN);


	if($xking ne $kid && $xgunshi ne $kid){&ERR("�����R�t�łȂ���Ύ��s�ł��܂���B");}

	if($xking eq $kid){
		$add = "�N��";
	}elsif($xgunshi eq $kid){
		$add = "�R�t";
	}

	@NEW_C_MES=();
	foreach(@C_MES){
		($mes,$cno)=split(/<>/);
		if($cno eq $kcon){
			$chit=1;
			push(@NEW_C_MES,"$in{'mes'}($add:$kname���)<>$kcon<>\n");
		}else{
			push(@NEW_C_MES,"$_");
		}
	}

	if(!$chit){
		unshift(@NEW_C_MES,"$in{'mes'}($add:$kname���)<>$kcon<>\n");
	}

	open(OUT,">$COUNTRY_MES");
	print OUT @NEW_C_MES;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>���U������͂��܂����B</h2><p>
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