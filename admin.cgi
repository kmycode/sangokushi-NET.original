#!/usr/bin/perl

#################################################################
#   �y�Ɛӎ����z                                                #
#    ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p���� #
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B         #
#    �܂��ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B   #
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B       #
#################################################################

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("�����e�i���X���ł��B���΂炭���҂����������B"); }
&DECODE;

if(!$ADMIN_SET) { &ERR2("�Ǘ��c�[�����g�p����ݒ�ɂȂ��Ă��܂���B"); }
	$adminid = "xxxx";
	$adminpass = "xxxx2";

if($mode eq 'CHANGE') { &CHANGE; }
elsif($mode eq 'MENTE') { &MENTE; }
elsif($mode eq 'MENTE2') { &MENTE2; }
elsif($mode eq 'CHANGE2') { &CHANGE2; }
elsif($mode eq 'BBS') { &BBS; }
elsif($mode eq 'DEL') { &DEL; }
elsif($mode eq 'DEL2') { &DEL2; }
elsif($mode eq 'DEL_LIST') { &DEL_LIST; }
elsif($mode eq 'ALL_DEL') { &ALL_DEL; }
elsif($mode eq 'INIT_DATA') { &INIT_DATA; }
else{&TOP;}


#_/_/_/_/_/_/_/_/_/#
#_/   MAIN���   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}


	&HEADER;

	print <<"EOM";

<h2>�Ǘ��c�[��</h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>�Ǘ����j���[</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=MENTE>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�L�����ҏW�P'>
</Th></form><TD>
�E�o�^�҂̃f�[�^��ҏW���܂��B�ʏ�͂�����ŕҏW���Ă��������B
�Q���҂̐���������Ǝg���Ȃ��Ȃ��\�\\��������܂��B
</TD></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=INIT_DATA>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='������'>
</Th></form><TD>
�E���ׂẴf�[�^�����������܂��B
</TD></TD></TR>

</TBODY></TABLE>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BBS>
MEMO:<input type=text name=message size=40>
NAME:<input type=text name=name size=10>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����'>
<br></form>

<form method="post" action="index.cgi">
</select><input type=submit value='�ҏW���I����'>
<br></form>
</CENTER>

EOM
	open(IN,"$ADMIN_BBS");
	@A_BBS = <IN>;
	close(IN);

	# �Ǘ��҃���
	print "<center><table width=80% border=0 >@A_BBS</table></center>";

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  MENTE���   _/#
#_/_/_/_/_/_/_/_/_/#

sub MENTE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	$i=0;
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			$datames = "�����F$dir/$file<br>\n";
			if(!open(page,"$dir/$file")){
				$datames .= "$dir/$file���݂���܂���B<br>\n";
				return 1;
			}
			@page = <page>;
			close(page);
			$list[$i]="$file";
			($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$page[0]);

			if("$in{'serch'}" ne ""){
				if("$ename" =~ "$in{'serch'}"){
					$human_data[$i]="$ehost<>$ename<>$eid<>";
				}else{
					next;
				}
			}else{
				if($in{'no'} eq "2"){
					$human_data[$i]="$ename<>$ehost<>$eid<>";
				}elsif($in{'no'} eq "3"){
					$human_data[$i]="$eid<>$ehost<>$ename<>";
				}else{
					$human_data[$i]="$ehost<>$ename<>$eid<>";
				}
			}
			push(@newlist,"@page<br>");
			$i++;
		}
	}
	closedir(dirlist);

	@human_data = sort @human_data;

	$tt = time - (60 * 60 * 24 * 34);
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
	$year += 1900;
	$mon++;
	$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
	$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);

	&HEADER;
	print <<"EOM";
<h2>�L�����Ǘ��c�[��</h2><br>
�EID�̓t�@�C�����Ɠ����ɂȂ��Ă���̂ŕύX���Ȃ��ŉ������B<br>
�E�z�X�g���͐����X�V���Ă��܂��B<br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE>�ҏW����t�@�C���F
<select name=fileno>
EOM
	$i=0;$w_host="";
	foreach(@human_data){
		if($in{'no'} eq "2"){
			($ename,$ehost,$eid) = split(/<>/);
		}elsif($in{'no'} eq "3"){
			($eid,$ehost,$ename) = split(/<>/);
		}else{
			($ehost,$ename,$eid) = split(/<>/);
		}
		print "<option value=$eid\.cgi>$eid $ename $ehost\n";
		if($in{'no'} eq "" || $in{'no'} eq "1"){
			if($w_host eq "$ehost"){
				$mess .= "$ename | $w_name<BR>\n";
			}
		}
		$w_host = "$ehost";
		$w_name = "$ename";
		$i++;
	}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�ҏW'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=MENTE>
<br><input type=radio name=no value="1">�z�X�g�����i<font color=red>2�d�o�^�`�F�b�N</font>�j<br>
<input type=radio name=no value="2">���O��<br>
<input type=radio name=no value="3">�h�c��<br>
���O����<input type=text name=serch size=20><br>
<input type=submit value='���ύX'>
<br></form>

<h2>�t�@�C������</h2>
�E�Q�d�o�^�҂������폜���܂��B<BR>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=DEL_LIST>
<input type=submit value='�폜�҃��X�g'>
<br></form>


�Q�d�o�^�^�f��<p>
<font color=red>$mess</font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='TOP'>
<br></form>

EOM
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
	print "@A_LOG";

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/_/_/#
#_/   DEL LIST���   _/#
#_/_/_/_/_/_/_/_/_/_/_/#

sub DEL_LIST {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}

	$tt = time - (60 * 60 * 24 * 34);
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
	$year += 1900;
	$mon++;
	$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
	$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	$i=0;
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			$datames = "�����F$dir/$file<br>\n";
			if(!open(page,"$dir/$file")){
				$datames .= "$dir/$file���݂���܂���B<br>\n";
				return 1;
			}
			@page = <page>;
			close(page);
			$list[$i]="$file";
			($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$page[0]);

			if($edate < $tt){
			$i++;
			($sec2,$min2,$hour2,$mday2,$mon2,$year2,$wday2,$yday2) = localtime($edate);
			$mon2++;
			$last_login = "$mon2��$mday2��$hour2��$min2��";
			$LIST .= "<TR><TD>$ename</TD><TD>$eid</TD><TD>$email</TD><TD>$last_login</TD></TR>";
			}
		}
	}
	closedir(dirlist);

	@human_data = sort @human_data;
	$a = "ss";
	$dir="./charalog/main";
	unlink("$dir/$a\.cgi");

	&HEADER;
	print <<"EOM";
<h2>�L�����Ǘ��c�[��</h2>
<br>

<h2>�t�@�C������</h2>
<TABLE><TBODY>
<TR><TD>���O</TD><TD>ID</TD><TD>MAIL</TD><TD>�ŏI�X�V</TD></TR>
$LIST
</TBODY></TABLE>

�����ȏ�̐l���폜���܂��B�X�����ł����H<BR>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=ALL_DEL>
<input type=submit value='�폜'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�߂�'>
<br></form>


EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ �t�@�C���폜 _/#
#_/_/_/_/_/_/_/_/_/#

sub ALL_DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}
	$tt = time - (60 * 60 * 24 * 34);

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	$i=0;
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			$datames = "�����F$dir/$file<br>\n";
			if(!open(page,"$dir/$file")){
				$datames .= "$dir/$file���݂���܂���B<br>\n";
			}
			@page = <page>;
			close(page);
			$list[$i]="$file";
			($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$emen,$eagi,$ecom,$egold,$e_ex,$ecex,$eunit,$econ,$earm,$epro,$eacc,$esub1,$esub2,$etac,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati) = split(/<>/,$page[0]);
			if($edate < $tt){
				$dir2="./charalog/main";
				unlink("$dir2/$eid\.cgi");
				$dir2="./charalog/bank";
				unlink("$dir2/$eid\.cgi");
				$dir2="./charalog/arm";
				unlink("$dir2/$eid\.cgi");
				$dir2="./charalog/item";
				unlink("$dir2/$eid\.cgi");
				$dir2="./charalog/chara_max";
				unlink("$dir2/$eid\.cgi");
				$dir2="./charalog/map";
				unlink("$dir2/$eid\.cgi");

				$i++;
			}
		}
	}
	closedir(dirlist);


	&HOST_NAME;

	&TIME_DATA;

	unshift(@S_MOVE,"<font color=red><B>\[�폜\]</B></font> �R�S���ȍ~���O�C���̂Ȃ������폜���܂����B($mday��$hour��$min��)<BR>\n");
	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG �V�����f�[�^���������߂܂���B');
	print OUT @S_MOVE;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>�R�S���ȍ~���O�C���̂Ȃ���(<font color=red>$i��</font>)���폜���܂����B</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�߂�'>
<br></form>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  WRITE���   _/#
#_/_/_/_/_/_/_/_/_/#

sub BBS {

	&TIME_DATA;
	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}

	open(IN,"$ADMIN_BBS");
	@AD_DATA = <IN>;
	close(IN);

	if($in{'message'} eq "") { &ERR2("���b�Z�[�W���L������Ă��܂���B"); }

	$bbs_num = @AD_DATA;
	if($bbs_num > 40) { pop(@AD_DATA); }

	unshift(@AD_DATA,"<font color=red>$in{'message'}</font> $in{'name'}���($mday��$hour��$min��)<BR><hr size=0>\n");

	open(OUT,">$ADMIN_BBS");
	print OUT @AD_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<h2>�������݂܂����B</h2>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='�߂�'>
<br></form>
EOM
	&FOOTER;
	exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/   �ҏW���   _/#
#_/_/_/_/_/_/_/_/_/#

sub CHANGE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}
	$dir="./charalog/main";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file���݂���܂���B<br>\n";
		return 1;
	}
	@page = <page>;
	close(page);
	
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$page[0]);
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($edate);
	$year += 1900;
	$mon++;
	$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
	$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);
	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><img src="$IMG/$echara.gif" width="$img_wid" height="$img_height" border=0> <font size=5 color=orange>$ename</font> �t�@�C��</h3>
<table>
<tr>
<th>ID</th><td><input type=text name=eid value='$eid'></td>
<th>PASS</th><td><input type=text name=epass value='$epass'></td>
<th>NAME</th><td><input type=text name=ename value='$ename'></td>
<th>�摜ID</th><td><input type=text name=echara value='$echara'></td>
<tr>
<th>����</th><td><input type=text name=estr value='$estr'></td>
<th>�m��</th><td><input type=text name=eint value='$eint'></td>
<th>������</th><td><input type=text name=elea value='$elea'></td>
<th>�l�]</th><td><input type=text name=echa value='$echa'></td>
</TR>
<tr>
<th>���m��</th><td><input type=text name=esol value='$esol'></td>
<th>�P��</th><td><input type=text name=egat value='$egat'></td>
<th>��</th><td><input type=text name=econ value='$econ'></td>
<th>��</th><td><input type=text name=egold value='$egold'></td>
</TR>
<tr>
<th>��</th><td><input type=text name=erice value='$erice'></td>
<th>�v��</th><td><input type=text name=ecex value='$ecex'></td>
<th>�K���l</th><td><input type=text name=eclass value='$eclass'></td>
<th>����</th><td><input type=text name=earm value='$earm'></td>
</TR>
<tr>
<th>����</th><td><input type=text name=ebook value='$ebook'></td>
<th>����</th><td><input type=text name=ebank value='$ebank'></td>
<th>�T�u�P</th><td><input type=text name=esub1 value='$esub1'></td>
<th>�T�u�Q</th><td><input type=text name=esub2 value='$esub2'></td>
</TR>
<tr>
<th>���݈ʒu</th><td><input type=text name=epos value='$epos'></td>
<th>���b�Z�[�W</th><td><input type=text name=emes value='$emes'></td>
<th>�z�X�g</th><td><input type=text name=ehost value='$ehost'></td>
<th>�X�V����</th><td><input type=text name=edate value='$edate'></td>
</TR>
<tr>
<th>MAIL</th><td><input type=text name=email value='$email'></td>
<th>�s���`�F�b�N</th><td><input type=text name=eos value='$eos'></td>
<th></th><td></td>
<th></th><td></td>
</TR>


</table>
<br>
<input type=hidden name=mode value=CHANGE2>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�ҏW'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�ҏW���~�߂�'>
</form>
<br>
<br>
<br>
<br>
MAP���O����<br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���̃t�@�C�����폜'>
</form>
<br>
<br>
<br>
MAP���O�Ȃ�<br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���̃t�@�C�����폜'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/   �ҏW���   _/#
#_/_/_/_/_/_/_/_/_/#

sub CHANGE2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}
	$dir="./charalog/main";
	
	$newdata = "$in{'eid'}<>$in{'epass'}<>$in{'ename'}<>$in{'echara'}<>$in{'estr'}<>$in{'eint'}<>$in{'elea'}<>$in{'echa'}<>$in{'esol'}<>$in{'egat'}<>$in{'econ'}<>$in{'egold'}<>$in{'erice'}<>$in{'ecex'}<>$in{'eclass'}<>$in{'earm'}<>$in{'ebook'}<>$in{'ebank'}<>$in{'esub1'}<>$in{'esub2'}<>$in{'epos'}<>$in{'emes'}<>$in{'ehost'}<>$in{'edate'}<>$in{'email'}<>$in{'eos'}<>\n";

	open(page,">$dir/$in{'fileno'}");
	print page $newdata;
	close(page);
	&HOST_NAME;
		
	&ADMIN_LOG("<font color=blue>$in{'ename'} $dir/$in{'fileno'}���X�V���܂����B�u$host�v</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$in{'ename'} �̃t�@�C��$dir/$in{'fileno'}���X�V���܂����B</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�߂�'>
</form>
EOM

	&FOOTER;
	exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/ �t�@�C���폜 _/#
#_/_/_/_/_/_/_/_/_/#

sub DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}
	&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR2('�t�@�C�����폜�ł��܂���ł����B');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);

	$dir2="./charalog/main";
	unlink("$dir2/$in{'filename'}");
	$dir2="./charalog/log";
	unlink("$dir2/$in{'filename'}");
	$dir2="./charalog/command";
	unlink("$dir2/$in{'filename'}");

	&ADMIN_LOG("<font color=red>$kname���폜���܂����B�u$host�v </font>");

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	&TIME_DATA;
	open(IN,"$DEF_LIST");
	@DEF_LIST = <IN>;
	close(IN);

	@NEW_DEF_LIST_DEL=();
	foreach(@DEF_LIST){
		($tid,$tname,$ttown_id,$ttown_flg,$tcon) = split(/<>/);
		if("$tid" eq "$kid"){
		}else{
			push(@NEW_DEF_LIST_DEL,"$_");
		}
	}
	open(OUT,">$DEF_LIST");
	print OUT @NEW_DEF_LIST_DEL;
	close(OUT);

	unshift(@S_MOVE,"<font color=red><B>\[�폜\]</B></font> $kname�͍폜����܂����B($mday��$hour��$min��)<BR>\n");
	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG �V�����f�[�^���������߂܂���B');
	print OUT @S_MOVE;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname���폜���܂����B</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�߂�'>
<br></form>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ �t�@�C���폜 _/#
#_/_/_/_/_/_/_/_/_/#

sub DEL2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}
&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR2('�t�@�C�����폜�ł��܂���ł����B');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);

	$dir2="./charalog/main";
	unlink("$dir2/$in{'filename'}");
	$dir2="./charalog/log";
	unlink("$dir2/$in{'filename'}");
	$dir2="./charalog/command";
	unlink("$dir2/$in{'filename'}");
	&ADMIN_LOG("<font color=red>$kname���폜���܂����B�u$host�v </font>");

	open(IN,"$DEF_LIST");
	@DEF_LIST = <IN>;
	close(IN);

	@NEW_DEF_LIST_DEL=();
	foreach(@DEF_LIST){
		($tid,$tname,$ttown_id,$ttown_flg,$tcon) = split(/<>/);
		if("$tid" eq "$kid"){
		}else{
			push(@NEW_DEF_LIST_DEL,"$_");
		}
	}
	open(OUT,">$DEF_LIST");
	print OUT @NEW_DEF_LIST_DEL;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname���폜���܂����B</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�߂�'>
<br></form>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ �Ǘ��҃��O   _/#
#_/_/_/_/_/_/_/_/_/#

sub ADMIN_LOG {

	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
	&TIME_DATA;

	unshift(@A_LOG,"$_[0]($mday��$hour��$min��)<BR>\n");
	splice(@A_LOG,20);

	open(OUT,">$ADMIN_LIST") or &ERR2('LOG �V�����f�[�^���������߂܂���B');
	print OUT @A_LOG;
	close(OUT);

}

#_/_/_/_/_/_/_/_/_/#
#_/   ������     _/#
#_/_/_/_/_/_/_/_/_/#

sub INIT_DATA {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�h�c�A�p�X���[�h�G���[ $num ");}

	require "reset.cgi";
	&RESET_MODE;
	&HOST_NAME;

	&ADMIN_LOG("�S�f�[�^�����������܂����B[$host]");
	
	&HEADER;
	print <<"EOM";
<h2><font color=red>�S�f�[�^�����������܂����B</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�߂�'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}


1;
