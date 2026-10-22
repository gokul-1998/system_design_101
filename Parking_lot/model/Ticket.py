"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Builder;
import lombok.Data;
import org.nailyourinterview.lld.parking_lot.enums.PaymentStatus;

import java.time.LocalDateTime;

@Data
@Builder
public class Ticket {
    private String ticketId;
    private LocalDateTime entryTime;
    private Vehicle vehicle;
    private String floorId;
    private String spotId;
    private PaymentStatus paymentStatus = PaymentStatus.PENDING;
}
"""


from dataclasses import dataclass, field
from datetime import datetime

from .vehicle import Vehicle
from ..enums.PaymentStatus import PaymentStatus


@dataclass
class Ticket:
    ticket_id: str
    entry_time: datetime
    vehicle: Vehicle
    floor_id: str
    spot_id: str
    payment_status: PaymentStatus = field(
        default=PaymentStatus.PENDING
    )
