#_/_/_/_/_/_/_/_/_/#
#_/    �����쐬  _/#
#_/_/_/_/_/_/_/_/_/#

sub MAKE_UNIT {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xcid eq "0"){&ERR("���������͎��s�ł��܂���B");}
	if($in{"name"} eq "������" || $in{"name"} eq ""){&ERR("���̖��O�͕t�����܂���B");}
	elsif($in{'name'} eq "" || length($in{'name'}) < 4 || length($in{'name'}) > 16) { &ERR("�������́A�Q�����ȏ�A�W�����ȉ��œ��͂��ĉ������B"); }
	elsif(length($in{'mes'}) > 40) { &ERR("������W�R�����g�́A�Q�O�����ȉ��œ��͂��ĉ������B"); }
	if($kclass < 500){&ERR("�v���l������܂���B");}

	open(IN,"$UNIT_LIST") or &ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@UNI_DATA = <IN>;
	close(IN);

	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($in{"name"} eq "$uunit_name"){&ERR("���̖��O�͊��ɑ��݂��܂��B");}
		if("$unit_id" eq "$kid"){&ERR("�������͕������쐬�ł��܂���B<BR>1�x���������U�����ĉ������B");}
		if("$uid" eq "$kid"){&ERR("�����ɏ������Ă���ꍇ�͕������쐬�ł��܂���B��������E�ނ��Ă��������B");}
	}

	if($kcex < ($READER_POINT * 10)){$pass = 0;}else{$pass = int($kcex / 10);}
	unshift(@UNI_DATA,"$kid<>$in{'name'}<>$kcon<>1<>$kid<>$kname<>$kchara<>$in{'mes'}<>0<>0<>\n");
	open(OUT,">$UNIT_LIST") or &ERR('UNIT1 �V�����f�[�^���������߂܂���B');
	print OUT @UNI_DATA;
	close(OUT);
	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$in{"name"}�������쐬���܂����B</h2><p>

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