"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PaymentMode {
    CASH, UPI, CARD
}
"""

from enum import Enum


class PaymentMode(Enum):
    CASH = "CASH"
    UPI = "UPI"
    CARD = "CARD"

    @classmethod
    def valueOf(cls, name: str):
        return cls[name]
