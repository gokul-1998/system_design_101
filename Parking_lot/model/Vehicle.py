
"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

@Getter
@RequiredArgsConstructor
public abstract class Vehicle {
    private final String number;
    private final VehicleType type;
}
"""



from abc import ABC
from dataclasses import dataclass

from ..enums.VehicleType import VehicleType


@dataclass
class Vehicle(ABC):
    number: str
    type: VehicleType
