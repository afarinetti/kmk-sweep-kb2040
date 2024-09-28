#!/usr/bin/env nu

use std log

def main [
    usb_drive: path
] {
    if ($usb_drive | path exists) {
        watch . --glob=*.py { | op, path, new_path | 
            match $op {
                "Write" => {
                    cp -v ($path | path basename) $usb_drive
                }
                _ => {
                    $"($op) ($path) ($new_path)"
                }
            }
        }
    } else {
        log error $"Path '($usb_drive)' is not found."
    }
}
