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
require './ini_file/i-index.ini';
require 'i-suport.pl';

if($MENTE) { &ERR("�����e�i���X���ł��B���΂炭���҂����������B"); }
&DECODE;
&TOP;

#_/_/_/_/_/_/_/_/_/#
#_/    TOP���   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	&CHARA_MAIN_OPEN;
	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	$p=0;
	foreach(@LOG_DATA){
		$log_list .= "<font color=navy>��</font>$LOG_DATA[$p]<BR>";$p++;
	}

	opendir(dirlist,"./charalog/main");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"./charalog/main/$file")){
				&ERR2("�t�@�C���I�[�v���G���[�I");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);



	$list = "<TR><TD></TD><TH>���O</TH><TH>����</TH><TH>�m��</TH><TH>������</TH><TH>���m��</TH><TH>����</TH></TR>";
	$num=0;
	foreach(@CL_DATA){
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if($epos eq $kpos){
			$num++;
			if($num < 100){
			$list .= "<TR><TD><img src=$IMG/$echara.gif></TD><TD>$ename</TD><TD>$estr</TD><TD>$eint</TD><TD>$elea</TD><TD>$esol</TD><TD>$cou_name[$econ]</TD></TR>";
			}
		}
	}
	&HEADER;
	print <<"EOM";
$log_list
<form action=\"i-status.cgi\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=STATUS><input type=submit value=\"�X�֖߂�\"></form>
EOM

	&FOOTER;
	exit;

}

