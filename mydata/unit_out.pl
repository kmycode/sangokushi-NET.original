#_/_/_/_/_/_/_/_/_/#
#_/    �����o�^  _/#
#_/_/_/_/_/_/_/_/_/#

sub UNIT_OUT {

	&CHARA_MAIN_OPEN;

	if($in{'did'} eq $kid){&ERR("�����͉��قł��܂���B");}

	open(IN,"$UNIT_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@UNI_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_UNI_DATA=();
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$unit_id" eq "$kid"){
			$hit=1;
			last;
		}
	}

	if(!$hit){
		&ERR("�����ȊO���s�ł��܂���B");
	}

	@NEW_UNI_DATA=();
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
			if("$uid" eq "$in{'did'}"){
				open(IN,"./charalog/main/$in{'did'}.cgi");
				@E_DATA = <IN>;
				close(IN);
				($eid,$epass,$ename) = split(/<>/,$E_DATA[0]);
				$mess = "$uunit_name��������$ename�����ق��܂����B";
			}else{
				push(@NEW_UNI_DATA,"$_");
			}
	}

	open(IN,"$MESSAGE_LIST") or &ERR('�t�@�C�����J���܂���ł����B');
	@MES_REG = <IN>;
	close(IN);

	$mes_num = @MES_REG;
	if($mes_num > $MES_MAX) { pop(@MES_REG); }
	unshift(@MES_REG,"$unit_id<>$kid<>$kpos<>$kname<><font color=FF0000>���F$mess<>$uname<>$daytime<>$kchara<>$kcon<>0<>\n");

	$mes_num = @MES_REG;
	if($mes_num > $MES_MAX) { pop(@MES_REG); }
	unshift(@MES_REG,"$eid<>$kid<>$kpos<>$kname<><font color=FF0000>���F$mess<>$ename<>$daytime<>$kchara<>$kcon<>0<>\n");
	open(OUT,">$MESSAGE_LIST") or &ERR('�t�@�C�����J���܂���ł����B');
	print OUT @MES_REG;
	close(OUT);

	open(OUT,">$UNIT_LIST") or &ERR('UNIT3 �V�����f�[�^���������߂܂���B');
	print OUT @NEW_UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$mess</h2><p>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�X�ɖ߂�"></form></CENTER>
EOM
	&FOOTER;
	exit;
}
1;