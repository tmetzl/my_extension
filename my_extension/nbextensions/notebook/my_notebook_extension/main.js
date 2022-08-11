define([
    // What do we want to import?
    "require",
    "jquery",
    "base/js/namespace",
    "base/js/events",
    "base/js/utils"
], function(
    // How do we name our imports?
    require, $, Jupyter, events, utils
) {

    function init() {
        alert("We loaded our notebook extension!");
        // Your code goes here!

        // Example of loading something from an external URL
        // First build the URL
        let url = utils.url_path_join(
            Jupyter.notebook.base_url, // The base url of the current server
            "myextension",
            "static",
            "js",
            "myfile.js"
        );

        // Then load the external resource
        require([url], function(myscript) {
            console.log("My external script was loaded!");
            console.log(myscript);
        });

    }

    /**
     * Hook for loading the extension
     * If the notebook is fully loaded the init function is called
     */
    function load_ipython_extension() {
        if (Jupyter.notebook !== undefined && Jupyter.notebook._fully_loaded) {
            init();
        } else {
            events.on("notebook_loaded.Notebook", init);
        }

    }

    return {
        load_ipython_extension: load_ipython_extension
    }
});