#_/_/_/_/_/_/_/_/_/#
#      ���ύX      #
#_/_/_/_/_/_/_/_/_/#

sub KING_COM4 {

	if($in{'sel'} eq "") { &ERR("�I������Ă��܂���"); }

	if($REFREE){
		$r_str = length("$SANGOKU_URL");
		$r_url = substr("$ENV{'HTTP_REFERER'}", 0, $r_str);
		if($r_url ne $SANGOKU_URL){ &ERR2("ERR No.002<BR>���̃L�����N�^�[�͍��܂���B<BR>�Ǘ��҂ɖ₢���킹�ĉ������B<BR>P1:$ROSER_URL <BR>P2:$r_url"); }
	}

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xking ne $kid){&ERR("���łȂ���Ύ��s�ł��܂���B");}

	$sel = $in{'sel'};
	open(IN,"./charalog/main/$sel\.cgi") or &ERR2('ID��PASS������������܂���I');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);	if($kcon ne "$econ") { &ERR("�s���ȏ����ł��B"); }
	if($kid eq "$eid") { &ERR("�s���ȏ����ł��B"); }

	&TIME_DATA;

	if($sel){
		$econ = 0;
		$res_mes = "$ename��$xname��������ق���܂����B";
		&MAP_LOG("<font color=880088><b>�y���فz</b></font>$ename��$xname��������ق���܂����B");
	}

	open(IN,"$LOG_DIR/black_list.cgi");
	@B_LIST = <IN>;
	close(IN);

	@NEW_B_LIST=();
	$hit=0;
	foreach(@B_LIST){
		($bid,$bcon,$bname,$bsub) = split(/<>/);
		if($bid eq $eid && $bcon eq $econ){
			$hit=1;
			push(@NEW_B_LIST,"$eid<>$econ<>$ename<><>\n");
		}else{
			push(@NEW_B_LIST,"$_");
		}
	}

	if(!$hit){
		unshift(@NEW_B_LIST,"$eid<>$econ<>$ename<><>\n");
	}

	open(OUT,">$LOG_DIR/black_list.cgi");
	print OUT @NEW_B_LIST;
	close(OUT);
	&ENEMY_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$res_mes</h2><p>
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