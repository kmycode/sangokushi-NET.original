#_/_/_/_/_/_/_/_/_/_/_/_/#
#        NEW_CHARA       #
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub NEW_CHARA {

	&CHEACKER;
	if ($CHARA_STOP) { &ERR2("���ݐV�K�o�^�͎󂯕t���Ă���܂���"); }
	if ($in{'id'} =~ m/[^0-9a-zA-Z]/) { &E_ERR("ID�ɔ��p�p�����ȊO�̕������܂܂�Ă��܂��B"); }
	if ($in{'pass'} =~ m/[^0-9a-zA-Z]/) { &E_ERR("�p�X���[�h�ɔ��p�p�����ȊO�̕������܂܂�Ă��܂��B"); }
	if ($in{'mail'} =~ /yahoo/ || $in{'mail'} =~ /hotmail/) { &E_ERR("���̃��[���A�h���X�͎g�p�ł��܂���B"); }
	if ($in{'mail'} eq "" || $in{'mail'} !~ /(.*)\@(.*)\.(.*)/){ &E_ERR("���[���̓��͂��s���ł��B");}
	if ($in{'id'} eq "" or length($in{'id'}) < 4 or length($in{'id'}) > 8) { &E_ERR("ID�́A4�����ȏ�A8�����ȉ��œ��͂��ĉ������B"); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 4 || length($in{'pass'}) > 8) { &E_ERR("�p�X���[�h�́A4�����ȏ�A8�����ȉ��œ��͂��ĉ������B"); }
	elsif($in{'con'} eq "") { &E_ERR("�����ʒu���I������Ă��܂���B"); }
	elsif($in{'mail'} eq "\@" || $in{'mail'} eq "") { &E_ERR("���[���̓��͂��s���ł�"); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 4 || length($in{'pass'}) > 16) { &E_ERR("�L�����N�^�[�̃p�X���[�h�����������͂���Ă��܂���B"); }
	elsif($in{'chara_name'} eq "" || length($in{'chara_name'}) < 4 || length($in{'chara_name'}) > 12) { &E_ERR("�L�����N�^�[�̖��O�����������͂���Ă��܂���B"); }
	elsif($in{'id'} eq $in{'pass'}) { &E_ERR("ID�ƃp�X���[�h�������ꍇ�A�o�^�͂ł��܂���"); }
	if ($in{'str'} =~ m/[^0-9]/) { &E_ERR("�͂ɐ����ȊO�̕������܂܂�Ă��܂��B"); }
	if ($in{'str'} eq "" || $in{'str'} < 5 || $in{'str'} > 100) { &E_ERR("�͂����������͂���Ă��܂���B");}
	if ($in{'int'} =~ m/[^0-9]/) { &E_ERR("�m�͂ɐ����ȊO�̕������܂܂�Ă��܂��B"); }
	if ($in{'int'} eq "" || $in{'int'} < 5 || $in{'int'} > 100) { &E_ERR("�m�͂����������͂���Ă��܂���B");}
	if ($in{'tou'} =~ m/[^0-9]/) { &E_ERR("�����͂ɐ����ȊO�̕������܂܂�Ă��܂��B"); }
	if ($in{'chara'} =~ m/[^0-9]/) { &E_ERR("�s���ł��B"); }
	if($in{'tou'} eq "" || $in{'tou'} < 5 || $in{'tou'} > 100) { &E_ERR("�����͂����������͂���Ă��܂���B");}

	$max = $in{'str'} + $in{'int'} + $in{'tou'};
	if($max ne "150"){
		&E_ERR("���v��\�\\�͂��P�T�O�ł͂���܂���B�i�v�F$max�j");
	}

	open(IN,"$TOWN_LIST") or &E_ERR("�w�肳�ꂽ�t�@�C�����J���܂���B");
	@TOWN_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &E_ERR('�t�@�C�����J���܂���ł����Berr no :country');
	@COU_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_NO_LIST") or &E_ERR('�t�@�C�����J���܂���ł����Berr no :country no');
	@COU_NO_DATA = <IN>;
	close(IN);

	$zc=0;$m_hit=0;
	($z2name,$z2con)=split(/<>/,$TOWN_DATA[$in{'con'}]);
	if($z2con eq ""){
		if($in{'ele'} eq ""){
			&E_ERR("�N��̏ꍇ���̐F��I�����Ă��������B");
		}elsif($in{'cou_name'} eq "" || length($in{'cou_name'}) < 2 || length($in{'cou_name'}) > 8) {
			&E_ERR("���̖��O�����������͂���Ă��܂���B");
		}
		$m_hit = 1;
		$cou_name = $in{'cou_name'};
		$new_cou_no = @COU_NO_DATA + 1;
		$hit = 1;
	}else{
		foreach(@COU_DATA){
			($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
			if($xcid eq $z2con){
				$cou_name = $xname;
				$kcon = $xcid;
				$hit = 1;
			}
		}
	}

	if(!$hit){
		&E_ERR("���̍��͑��݂��܂���B");
	}

	&SET_COOKIE;
	&HOST_NAME;

	$date = time();
	$pos = 2;
	open(IN,"./charalog/main/$in{'id'}.cgi");
	@NEWCHARA = <IN>;
	close(IN);

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&E_ERR("�t�@�C���I�[�v���G���[�I");
			}
			@page = <page>;
			close(page);
			push(@REGIST_VI,"@page<br>");
		}
	}
	closedir(dirlist);

	$hit=0;@new_chara=();
	($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos) = split(/<>/,$NEWCHARA[0]);

	if($rkid eq "$in{'id'}") {&E_ERR("����ID�͓o�^�ς݂ł��B�ႤID��I�����Ă��������B");}

	if($REFREE){
		if($ENV{'HTTP_REFERER'} ne "$SANGOKU_URL/$FILE_ENTRY" && $ENV{'HTTP_REFERER'} ne "$SANGOKU_URL/$FILE_TOP" && $ENV{'HTTP_REFERER'} ne "$SANGOKU_URL/"){ &E_ERR("ERR No.001<BR>���̃L�����N�^�[�͍��܂���B<BR>�Ǘ��҂ɖ₢���킹�ĉ������B<BR>P1:$ROSER_URL/$FILE_ENTRY<BR>P2$ENV{'HTTP_REFERER'}"); }
	}
	foreach(@REGIST_VI){
		($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos) = split(/<>/);
		if($ACCESS){
			if($host eq $rkhost ){
				&E_ERR("��l�ɂ��P�L�����N�^�[�ł��B�������͓���IP�̕������ɓo�^���Ă��܂��B");
			}
		}
		if($rkname eq "$in{'chara_name'}"){
			&E_ERR("���̖��O�͊��ɓo�^����Ă��܂��B�Ⴄ���O�œo�^���Ă��������B");
		}
		if($rkmail eq "$in{'mail'}"){
			&E_ERR("���̃��[���A�h���X�͊��ɓo�^����Ă��܂��B");
		}
		if($kcon eq $rkcon){
			$con_num++;
		}
	}

	if($xmark < $BATTLE_STOP && $con_num >= $CON_ENTRY_MAX){
		&E_ERR("���̍��͒���𒴂��Ă���̂œ����ł��܂���B");
	}
	if($m_hit){
		$kcon = $new_cou_no;
		$month_read = "$LOG_DIR/date_count.cgi";
		open(IN,"$month_read") or &E_ERR('�t�@�C�����J���܂���ł����B');
		@MONTH_DATA = <IN>;
		close(IN);
		($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
		$old_date = sprintf("%02d\�N%02d\��", $F_YEAR+$myear, $mmonth);

		push(@COU_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><>$in{'chara_name'}<>1<>\n");
		open(OUT,">$COUNTRY_LIST") or &E_ERR('COUNTRY �f�[�^���������߂܂���B');
		print OUT @COU_DATA;
		close(OUT);

		push(@COU_NO_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><><>1<>\n");
		open(OUT,">$COUNTRY_NO_LIST") or &E_ERR('COUNTRY �f�[�^���������߂܂���B');
		print OUT @COU_NO_DATA;
		close(OUT);

		&TOWN_DATA_OPEN("$in{'con'}");
		$zcon = $new_cou_no;
		&TOWN_DATA_INPUT;
		&MAP_LOG2("<font color=000088><B>�y�����z</B></font>\[$old_date\]�V����$in{'chara_name'}��$cou_name�����������܂����B");
		&MAP_LOG("<font color=000088><B>�y�����z</B></font>�V����$in{'chara_name'}��$cou_name�����������܂����B");

	}else{
		&MAP_LOG("<font color=0088CC><B>\[�d��\]</B></font>�V����$in{'chara_name'}��$cou_name���Ɏd�����܂����B");
	}

	@NEW_COM=();
	for($i=0;$i<$MAX_COM;$i++){
		push(@NEW_COM,"<><><>$tt<><><>50<>\n");
	}

	open(OUT,">./charalog/command/$in{'id'}.cgi");
	print OUT @NEW_COM;
	close(OUT);

	if($ATTESTATION){
		&mail_to;
		$os = 0;
	}else{
		$os = 1;
	}

	$kcha = int(rand(101));
	$ksol = 0;
	$kgat = 0;
	$kgold = 1000;
	$krice = 500;
	$kcex = 0;
	$kclass = 0;
	$karm = 0;
	$kbook = 0;
	$kbank = "";
	$ksub1 = "";
	$ksub2 = $DEL_TURN - 10;
	$kstr = $in{'str'}+0;
	$kint = $in{'int'}+0;
	$ktou = $in{'tou'}+0;

	unshift(@new_chara,"$in{'id'}<>$in{'pass'}<>$in{'chara_name'}<>$in{'chara'}<>$kstr<>$kint<>$ktou<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$in{'con'}<>$in{'mes'}<>$host<>$date<>$in{'mail'}<>$os<>\n");
	open(OUT,">./charalog/main/$in{'id'}.cgi");
	print OUT @new_chara;
	close(OUT);

	&DATA_SEND;
	exit;
}


#------------------#
#  ���[�����M����  #
#------------------#
sub mail_to {
	unless (-e $SENDMAIL) { &E_ERR("sendmail�̃p�X���s���ł�"); }

	# ���[���^�C�g��
	$mail_sub = " �o�^�����ʒm";
	&TIME_DATA;

	$a_pass = crypt("$in{'pass'}", $ATTESTATION_ID);
	# ���[���{��
	$mail_msg = <<"EOM";
$in{'chara_name'} �l

���̓x�́A$GAME_TITLE �ւ̓o�^�����肪�Ƃ��������܂����B
�o�^���e�͈ȉ��̂Ƃ���ł��̂ŁA���m�F���������B

���o�^�����F$daytime
���z�X�g���F$host
���Q���Җ��F$in{'chara_name'}
���d���[���F$in{'mail'}
���h�c    �F$in{'id'}
���o�`�r�r�F$in{'pass'}
���F�؃L�[�F$a_pass

�F�؃L�[��o�^���邱�Ƃɂ���ăQ�[���ɎQ�����邱�Ƃ���
���܂��B

[�F�؃L�[�̐ݒ�]
$SANGOKU_URL/entry.cgi?mode=ATTESTATION
(�������炩��o�^���o���܂��B)

�悭�Q���K����悭�ǂ�ł���Q�[�����J�n���Ă��������B
�܂��A�p�X���[�h�A�h�c���̍Ĕ��s�͒v���܂���̂ő�؂�
�ۊǂ��Ă����ĉ������B

_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
$GAME_TITLE�Ǘ��l
  Home:   $HOME_URL
EOM
	# JIS�R�[�h�֕ϊ�
    	&jcode'convert(*mail_sub,'jis');
    	&jcode'convert(*mail_msg,'jis');

	# �R�����g���̉��s�ƃ^�O�𕜌�
	$mail_msg =~ s/<br>/\n/ig;

	# ���[������
	open(MAIL,"| $SENDMAIL -t") || &E_ERR("���[�����M�Ɏ��s���܂���");
	print MAIL "To: $in{'mail'}\n";
	print MAIL "Subject: $mail_sub\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-type: text/plain; charset=ISO-2022-JP\n";
	print MAIL "Content-Transfer-Encoding: 7bit\n";
	print MAIL "X-Mailer: $ver\n\n";
	print MAIL "$mail_msg\n";
	close(MAIL);

}
#_/_/_/_/_/_/_/_/#
#  ERROR PRINT   #
#_/_/_/_/_/_/_/_/#

sub E_ERR {

	&HEADER;
	if (-e $lockfile) { unlink($lockfile); }
	print "<center><hr size=0><h3>ERROR !</h3>\n";
	print "<P><font color=red><B>$_[0]</B></font>\n";
	print "<form action=\"$FILE_ENTRY\" method=\"post\"><input type=hidden name=id value=$in{'id'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=mail value=$in{'mail'}><input type=hidden name=url value=$in{'url'}><input type=hidden name=chara_name value=$in{'chara_name'}><input type=hidden name=mes value=$in{'mes'}><input type=hidden name=mode value=entry><input type=submit value=\"���͂ɖ߂�\"></form>";
	print "<P><hr size=0></center>\n</body></html>\n";
	exit;
}
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/   �Q���o�^�ҏ���`�F�b�N   _/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("�t�@�C���I�[�v���G���[�I");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	$num = @CL_DATA;

	if($ENTRY_MAX){
		if($num > $ENTRY_MAX){
			&ERR2("�ő�o�^��\[$ENTRY_MAX\]�𒴂��Ă��܂��B���ݐV�K�o�^�o���܂���B");
		}
	}
}

1;