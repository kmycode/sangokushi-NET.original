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
require 'i-suport.pl';

if($MENTE) { &ERR2("�����e�i���X���ł��B���΂炭���҂����������B"); }
&DECODE;
&TOP;

#_/_/_/_/_/_/_/_/_/#
#_/    TOP���   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	$date = time();
	$month_read = "$LOG_DIR/date_count.cgi";
	open(IN,"$month_read") or &ERR2('�t�@�C�����J���܂���ł����B');
	@MONTH_DATA = <IN>;
	close(IN);

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$S_MES .= "<font color=008800>��</font>$S_MOVE[$p]<BR>";$p++;}

	$hit = 0;
	@month_new=();

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);


	$MESS1 = "<A href=\"$FILE_CONTNUE\">�yCONTNUE�z</a>";
	$MESS2 = "<A href=\"$FILE_ENTRY\">�yNEW GAME�z</a>";
	&roses_counter;
	$new_date = sprintf("%02d\�N%02d\��", $F_YEAR+$myear, $mmonth);
	$next_time = int(($mtime + $TIME_REMAKE - $date) / 60);

	&HEADER;
	print <<"EOM";
<CENTER>
�y  $GAME_TITLE  �z<BR>
[$new_date]<BR>
����̍X�V�܂� $next_time ��<BR>
<form action="./i-status.cgi" method="POST"><input type="hidden" name="mode" value="STATUS">USER ID<input type="text" size="10" name="id" value="$_id"><BR>
PASS WORD<input type="password" size="10" name="pass" value="$_pass"><BR>
<input type="submit" value="���O�C��"></form>
TOTAL ACCESS $total_count HIT.<p>
$S_MES
EOM

	&FOOTER;
	exit;

}

sub roses_counter {

	$file_read = "$LOG_DIR/counter.cgi";
	open(IN,"$file_read") or &ERR2('�t�@�C�����J���܂���ł����B');
	@reading = <IN>;
	close(IN);

	($total_count) = split(/<>/,$reading[0]);
	$total_count++;

	open(OUT,">$file_read");
	print OUT "$total_count\n";
	close(OUT);

}


