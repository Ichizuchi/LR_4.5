#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import os
from pathlib import Path
from typing import List, Dict, Any

# Имя файла данных по умолчанию
default_data_file = "flights.json"

def input_flights() -> List[Dict[str, str]]:
    flights: List[Dict[str, str]] = []
    n: int = int(input("Введите количество рейсов: "))

    for i in range(n):
        flight: Dict[str, str] = {}
        flight["город назначения"] = input("Введите город назначения: ")
        flight["номер рейса"] = input("Введите номер рейса: ")
        flight["тип самолета"] = input("Введите тип самолета: ")
        flights.append(flight)

    flights.sort(key=lambda x: x["город назначения"])
    return flights

def print_flights_with_plane_type(flights: List[Dict[str, str]]) -> None:
    plane_type: str = input("Введите тип самолета: ")
    found: bool = False
    for flight in flights:
        if flight["тип самолета"] == plane_type:
            print(f"Город назначения: {flight['город назначения']}, Номер рейса: {flight['номер рейса']}")
            found = True
    if not found:
        print("Рейсы с указанным типом самолета не найдены")

def save_data_to_json(flights: List[Dict[str, str]], data_file: Path) -> None:
    with open(data_file, 'w', encoding='utf-8') as file:
        json.dump(flights, file, ensure_ascii=False)

def load_data_from_json(data_file: Path) -> List[Dict[str, Any]]:
    if os.path.exists(data_file):
        with open(data_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []

def main() -> None:
    parser = argparse.ArgumentParser(description='Manage flight data')
    parser.add_argument('--input', action='store_true', help='Input new flight data')
    parser.add_argument('--print_plane_type', action='store_true', help='Print flights with specific plane type')
    args = parser.parse_args()

    # Получаем путь к домашнему каталогу пользователя
    home_dir = Path.home()
    data_file = home_dir / "flights.json"

    if args.input:
        flights = input_flights()
    else:
        flights = load_data_from_json(data_file)

    if args.print_plane_type:
        print_flights_with_plane_type(flights)

    save_data_to_json(flights, data_file)

if __name__ == "__main__":
    main()
