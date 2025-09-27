def check_fire(temperature, smoke):
    """Check thresholds for fire detection"""
    fire_detected = False
    alert_message = "Safe ✅"

    if temperature > 60 or smoke > 70:
        fire_detected = True
        alert_message = "🚨 FIRE DETECTED! 🚨 Buzzer ON 🔔"

    return fire_detected, alert_message
