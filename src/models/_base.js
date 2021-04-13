import _ from 'lodash';

class BaseModel {
    constructor(data = {}) {
        let defaults = this.defaults;
        // take only allowed properties
        let attributes = _.pick(data, _.keys(defaults));
        // fill instance's attributes
        _.defaultsDeep(this, attributes, defaults);
    }

    /**
     * Returns possible keys and their default values
     *
     * @returns {object}
     */
    get defaults() {
        return {};
    }

    /**
     * Converts list of raw-data into list of models
     *
     * @param {array} list
     * @returns {array}
     */
    static list(list) {
        return list.map(item => new this(item))
    }
}

export default BaseModel;