$(document).ready(function() {
    function updateDepartmentSelect(departments) {
        var departmentSelect = $("#id_department");
        departmentSelect.empty();
        departmentSelect.append($('<option>', {
            value: "",
            text: "Выберите отдел",
            selected: true,
            disabled: true
        }));
        departments.forEach(function(dep) {
            departmentSelect.append($('<option>', {
                value: dep.id,
                text: dep.name + " отдел"
            }));
        });
    }

    function updateSectorSelect(sectors) {
        var sectorSelect = $("#id_sector");
        sectorSelect.empty();
        sectorSelect.append($('<option>', {
            value: "",
            text: "Выберите сектор",
            selected: true,
            disabled: true
        }));
        sectors.forEach(function(sec) {
            sectorSelect.append($('<option>', {
                value: sec.id,
                text: sec.name + " сектор"
            }));
        });
    }

    $("#id_management").change(function() {
        var managementId = $(this).val();
        var departmentsUrl = $(this).data('get-departments-url');  // Получаем URL для запроса отделов
        $.ajax({
            url: departmentsUrl,
            data: { management_id: managementId },
            success: function(data) {
                updateDepartmentSelect(data);
                updateSectorSelect([]);
            }
        });
    });

    $("#id_department").change(function() {
        var departmentId = $(this).val();
        if (!departmentId) {
            return;
        }
        var sectorsUrl = $(this).data('get-sectors-url');  // Получаем URL для запроса секторов
        $.ajax({
            url: sectorsUrl,
            data: { department_id: departmentId },
            success: function(data) {
                updateSectorSelect(data);
        }
        });
    });

    });


