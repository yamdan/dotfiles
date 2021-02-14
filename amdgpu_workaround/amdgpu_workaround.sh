#!/bin/sh

echo "manual" > /sys/class/drm/card0/device/power_dpm_force_performance_level
echo 0 > /sys/class/drm/card0/device/pp_dpm_mclk
echo 0 > /sys/class/drm/card0/device/pp_dpm_sclk
