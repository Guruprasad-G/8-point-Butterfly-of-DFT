const {spawn} = require('child_process');

exports.fetchanswer = async (req,res) => {
    try{
        const dft = await spawn('python', ['./py files/butterfly_fft.py']);
        dft.stdout.on('data', function(data){
            console.log("Data received from Python file = ",data);
        })
        res.send(data);
    } catch (err) {{
        res.status(404).json({
            status: 'Failed',
            message: err,
            })
        }
    }
}

