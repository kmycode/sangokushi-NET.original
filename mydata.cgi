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
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("�A�h���X�o�[�ɒl����͂��Ȃ��ł��������B"); }
if($mode eq 'MES_SEND') { require 'mydata/mes_send.pl';&MES_SEND; }
elsif($mode eq 'COUNTRY_TALK') { require 'mydata/country_talk.pl';&COUNTRY_TALK; }
elsif($mode eq 'COUNTRY_WRITE') { require 'mydata/country_write.pl';&COUNTRY_WRITE; }
elsif($mode eq 'LOCAL_RULE') { require 'mydata/local_rule.pl';&LOCAL_RULE; }
elsif($mode eq 'L_RULE_WRITE') { require 'mydata/l_rule_write.pl';&L_RULE_WRITE; }
elsif($mode eq 'L_RULE_DEL') { require 'mydata/l_rule_del.pl';&L_RULE_DEL; }


elsif($mode eq 'COU_CHANGE') { require 'mydata/cou_change.pl';&COU_CHANGE; }
elsif($mode eq 'CYUUSEI') { require 'mydata/cyuusei.pl';&CYUUSEI; }
elsif($mode eq 'LETTER') { require 'mydata/letter.pl';&LETTER; }
elsif($mode eq 'KING_COM') { require 'mydata/king_com.pl';&KING_COM; }
elsif($mode eq 'KING_COM2') { require 'mydata/king_com2.pl';&KING_COM2; }
elsif($mode eq 'KING_COM3') { require 'mydata/king_com3.pl';&KING_COM3; }
elsif($mode eq 'KING_COM4') { require 'mydata/king_com4.pl';&KING_COM4; }
elsif($mode eq 'KING_COM5') { require 'mydata/king_com5.pl';&KING_COM5; }

elsif($mode eq 'UNIT_ENTRY') { require 'mydata/unit_entry.pl';&UNIT_ENTRY; }
elsif($mode eq 'UNIT_SELECT') { require 'mydata/unit_select.pl';&UNIT_SELECT; }
elsif($mode eq 'UNIT_OUT') { require 'mydata/unit_out.pl';&UNIT_OUT; }
elsif($mode eq 'MAKE_UNIT') { require 'mydata/make_unit.pl';&MAKE_UNIT; }
elsif($mode eq 'UNIT_DELETE') { require 'mydata/unit_delete.pl';&UNIT_DELETE; }
elsif($mode eq 'UNIT_CHANGE') { require 'mydata/unit_change.pl';&UNIT_CHANGE; }

else{&ERR('�������I������Ă��܂���B');}

