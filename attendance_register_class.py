class attendance:
    records = {}
    def mark_present(name):
        attendance.records[name] = "present"
    def mark_absent(name):
        attendance.records[name] = "absent"
    def get_status(name):
        if name in attendance.records:
            return attendance.records[name]
        else:
            return "not marked"
    def show_register():
        return attendance.records
register = attendance
register.mark_present("john")
register.mark_absent("mary")
print(register.get_status("john"))
print(register.get_status("peter"))
print(register.show_register())
