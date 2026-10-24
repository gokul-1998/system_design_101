"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum GateType {
    ENTRY,
    EXIT
}
"""

from enum import Enum


class GateType(Enum):
    ENTRY = "ENTRY"
    EXIT = "EXIT"

    @classmethod
    def valueOf(cls, name: str):
        return cls[name]
