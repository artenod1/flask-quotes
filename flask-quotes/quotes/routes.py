from flask import render_template, url_for, flash, redirect
from quotes.models import Quote
from quotes.forms import QuoteForm
from quotes import app, db



@app.route("/", methods=['GET'])
def home():
    quotes = Quote.query.all()
    return render_template('home.html', quotes=quotes)


@app.route("/new", methods=['GET', 'POST'])
def new_quote():
    form = QuoteForm()
    if form.validate_on_submit():
        quote = Quote(quote=form.quote.data, quote_origin=form.quote_origin.data)
        db.session.add(quote)
        db.session.commit()
        flash('Your quote has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('create_quote.html', title="New quote", form=form)

@app.route("/quote/<int:quote_id>")
def quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    return render_template('quote.html', quote=quote)

@app.route("/quote/<int:quote_id>/update", methods=['GET', 'POST'])
def update_quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    form = QuoteForm()
    if form.validate_on_submit():
        quote.quote = form.quote.data
        quote.quote_origin = form.quote_origin.data
        db.session.commit()
        flash('Your quote has been updated!', 'success')
        return redirect(url_for('quote', quote_id=quote.id))
    # elif request.method == 'GET':
    #     form.title.data = quote.title
    #     form.content.data = quote.content
    return render_template('create_quote.html', title='Update Quote',
                           form=form, legend='Update Quote')


@app.route("/quote/<int:quote_id>/delete", methods=['POST'])
def delete_quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    db.session.delete(quote)
    db.session.commit()
    flash('Your quote has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/api/all-quotes")
def get_all_quotes():
    quotes = Quote.query.all()
    output = []
    for q in quotes:
        quote_data = {
            'quote_id': q.id,
            'quote': q.quote,
            'quote_origin': q.quote_origin,
            'date_posted': q.date_posted
        }
        output.append(quote_data)

    return {"data": output}