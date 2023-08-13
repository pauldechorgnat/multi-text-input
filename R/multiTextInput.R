# AUTO GENERATED FILE - DO NOT EDIT

#' @export
multiTextInput <- function(id=NULL, label=NULL, placeholder=NULL, value=NULL, values=NULL) {
    
    props <- list(id=id, label=label, placeholder=placeholder, value=value, values=values)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MultiTextInput',
        namespace = 'multi_text_input',
        propNames = c('id', 'label', 'placeholder', 'value', 'values'),
        package = 'multiTextInput'
        )

    structure(component, class = c('dash_component', 'list'))
}
