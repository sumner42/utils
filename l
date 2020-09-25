#!/bin/bash
ls -lF --color=auto $@ | cut -c1-14,33-140
