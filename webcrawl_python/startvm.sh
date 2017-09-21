#!/bin/bash

if ([ $# -eq 0 ]) then
    echo "Usage: $0 <Enter the vm names with space>"
    exit 1
fi

VBoxManage startvm $* --type headless
