

let catform = $('#catform');
catform.submit((e) => {
    e.preventDefault();
    $.ajax({
        type: "post",
        url: "/api/category/create/",
        data: catform.serialize(),
        dataType: "json",
        success: function (response) {
            status = response.status;
            id = response.id;
            name = response.name;
            if (status === 'success') {
                // alert('Category Added Successfully');
                let category = $('#id_category');
                category.append(`<option value="${id}">${name}</option>`);
                catform.find('input').val('');
                // add a tick mark in the form
                catform.append(`<i class="bi bi-check-circle-fill text-success px-3"></i>`);
                // timeout to remove the tick mark
                setTimeout(() => {
                    tagform.find('i').remove();
                }, 2000);
            }
            else {
                alert(status);
            }
        }
    });
});

let tagform = $('#tagform');
tagform.submit((e) => {
    e.preventDefault();
    $.ajax({
        type: "post",
        url: "/api/tag/create/",
        data: tagform.serialize(),
        dataType: "json",
        success: function (response) {
            status = response.status;
            id = response.id;
            name = response.name;
            if (status === 'success') {
                let tags = $('#id_tags');
                tag_checkbox_snippet = `<div class="form-check">
                <input class="form-check-input" type="checkbox" name="tags" id="id_tags_${id - 1}" value="${id}">
                <label class="form-check-label" for="id_tags_${id - 1}">${name}</label>
                </div>
                `
                tags.append(tag_checkbox_snippet);
                tagform.find('input').val('');
                // add a tick mark in the form
                tagform.append(`<i class="bi bi-check-circle-fill text-success px-3"></i>`);
                // timeout to remove the tick mark
                setTimeout(() => {
                    tagform.find('i').remove();
                }, 2000);
            }
            else {
                alert(status);
            }
        }
    });
});

let mediaform = $('#media-form');
mediaform.submit((e) => {
    e.preventDefault();
    $.ajax({
        type: "post",
        url: "/api/image/upload/",
        data: new FormData(mediaform[0]),
        processData: false,
        contentType: false,
        success: function (response) {
            status = response.status;
            id = response.id;
            name = response.name;
            if (status === 'success') {
                let media = $('#id_media');
                media.append(`<option value="${id}">${name}</option>`);
                mediaform.find('input').val('');
                // add a tick mark in the form
                mediaform.append(`<i class="bi bi-check-circle-fill text-success px-3"></i>`);
                // timeout to remove the tick mark
                setTimeout(() => {
                    mediaform.find('i').remove();
                }, 2000);
            }
            else {
                alert(status);
            }
        }
    });
});