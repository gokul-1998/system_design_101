"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PaymentStatus {
    PENDING,
    SUCCESS,
    FAILED
}
"""

from enum import Enum


class PaymentStatus(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

    @classmethod
    def valueOf(cls, name: str):
        return cls[name]
