import BaseModel from './_base.js';

class Playlist extends BaseModel {
    constructor(props) {
        super(props);

        this.createdAt = this.createdAt ? new Date(this.createdAt) : null;
        this.updatedAt = this.updatedAt ? new Date(this.updatedAt) : null;
    }

    get defaults() {
        return {
            id: null,
            name: null,
            createdAt: null,
            updatedAt: null,
        };
    }
}

export default Playlist;