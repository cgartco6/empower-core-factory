#!/bin/bash

ISO_NAME=empower_factory.iso
WORKDIR=iso_root

mkdir -p $WORKDIR
cp -r installers core-factory docker $WORKDIR

sha256sum $(find $WORKDIR -type f) > $WORKDIR/manifest.sha256

mkisofs -o $ISO_NAME -V "EMPOWER_AI_FACTORY" $WORKDIR
