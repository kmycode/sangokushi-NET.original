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

if($mode eq "") {require 'entry/entry.pl'; &ENTRY; }
elsif($mode eq 'NEW_CHARA') { require 'entry/new_chara.cgi';require 'entry/data_send.pl';&NEW_CHARA; }
elsif($mode eq 'DATA_SEND') { require 'entry/data_send.pl';&DATA_SEND; }
elsif($mode eq 'RESISDENTS') { require 'entry/resisdents.pl';&RESISDENTS; }
elsif($mode eq 'ATTESTATION') { require 'entry/attestation.cgi';&ATTESTATION; }
elsif($mode eq 'SET_ENTRY') { require 'entry/attestation.cgi';&SET_ENTRY; }
else{require 'entry/entry.pl';&ENTRY;}

