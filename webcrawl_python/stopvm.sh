#!/bin/sh

if ([ $# -eq 0 ]) then
    echo "Usage: $0 <Enter the vm name with space>"
    exit 1
fi

VBoxManage controlvm $* poweroff
